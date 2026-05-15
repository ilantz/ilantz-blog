import os
import re
import yaml
import argparse

def detect_code_language(code_content):
    """
    Heuristically detect if code content is PowerShell, XML, CMD, or Registry.
    Returns the detected language or 'text'.
    """
    # Remove any existing fences if we're analyzing inner content
    code_content = re.sub(r'^```\w*\n', '', code_content)
    code_content = re.sub(r'\n```$', '', code_content)

    # Detect Registry
    reg_score = 0
    if re.search(r'\b(HKEY_LOCAL_MACHINE|HKEY_CURRENT_USER|HKEY_CLASSES_ROOT|HKEY_USERS|HKEY_CURRENT_CONFIG)\b', code_content, re.IGNORECASE): reg_score += 5
    if re.search(r'\b(HKLM|HKCU|HKCR|HKU|HKCC)\b', code_content): reg_score += 3
    if re.search(r'\[DWORD\]', code_content, re.IGNORECASE): reg_score += 2
    if re.search(r'^[a-z0-9_\s\\-]+(\s+)?=', code_content, re.MULTILINE | re.IGNORECASE) and reg_score > 0: reg_score += 2
    if re.search(r'\\\w+', code_content) and reg_score > 0: reg_score += 1 # Path separators

    # Detect PowerShell
    ps_score = 0
    if re.search(r'\$\w+', code_content): ps_score += 1
    if re.search(r'\b(Get|Set|Invoke|Add|Remove|New|Select|Where|Write|Out|Test|Export|Import|Start|Stop|Restart)-\w+\b', code_content, re.IGNORECASE): ps_score += 2
    if re.search(r'\|', code_content): ps_score += 1
    if re.search(r'-\w+\s+', code_content): ps_score += 1 
    if re.search(r'\b(Read-Host|Write-Host|New-Object|ForEach-Object|ConvertFrom-Json)\b', code_content, re.IGNORECASE): ps_score += 3

    # Detect XML
    xml_score = 0
    if re.search(r'<\?xml', code_content, re.IGNORECASE): xml_score += 5
    # Stricter tag detection to avoid <or> or <name> in text
    if re.search(r'<[a-zA-Z][\w:-]*(\s+[\w:-]+(\s*=\s*("[^"]*"|\'[^\']*\'))?)*\s*>', code_content) and re.search(r'</[a-zA-Z][\w:-]*>', code_content): xml_score += 4
    if re.search(r'xmlns[:=]', code_content): xml_score += 3
    if re.search(r'<[a-zA-Z]+(\s+[a-zA-Z]+="[^"]*")*\s*/>', code_content): xml_score += 3 # Self-closing tags

    # Detect CMD / Batch
    cmd_score = 0
    if re.search(r'\b(reg|msiexec|regedit|ipconfig|netstat|ping|tracert|net|dir|copy|move|del|cls|echo|pause)\b', code_content, re.IGNORECASE): cmd_score += 2
    if re.search(r'\b(reg\s+(add|query|delete|copy|save|restore|load|unload|compare|export|import|flags))\b', code_content, re.IGNORECASE): cmd_score += 5
    if re.search(r'/[a-z]\b', code_content, re.IGNORECASE): cmd_score += 1 # Flags like /i, /f
    if re.search(r'REINSTALLMODE=', code_content): cmd_score += 5

    # Detect Claims Rules (ADFS)
    claims_score = 0
    if re.search(r'c:\[Type == ".*?"\] => issue\(Type = ".*?"', code_content): claims_score += 10

    scores = {
        'registry': reg_score,
        'powershell': ps_score,
        'xml': xml_score,
        'cmd': cmd_score,
        'claims': claims_score
    }
    
    best_lang = max(scores, key=scores.get)
    if scores[best_lang] >= 2:
        if best_lang == 'claims': return 'text'
        return best_lang
    
    return 'text'

def fix_mangled_paths(content):
    # Fix [\\path](///) -> \\path
    return re.sub(r'\[(\\\\.*?)\]\(///\)', r'\1', content)

def normalize_fences(content):
    # Logic to fix malformed fences and unclosed blocks
    content = re.sub(r'\[\s*```(\w*)', r'\n```\1\n', content)
    content = re.sub(r'```(\w*)\s*\]', r'\n```\n', content)
    content = re.sub(r'`\s*```(\w*)', r'\n```\1\n', content)
    content = re.sub(r'```\s*`', r'\n```\n', content)
    
    lines = content.split('\n')
    result = []
    in_code_block = False
    code_buffer = []
    block_lang = 'text'

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('``') and not stripped.startswith('```'):
            lang = re.sub(r'[`\[\]]', '', stripped.replace('```', '').replace('``', '')).strip().lower()
            if not in_code_block:
                in_code_block = True
                block_lang = lang or 'text'
                code_buffer = []
            else:
                if any(l.strip() and not l.strip().startswith('`') for l in code_buffer):
                    result.append(f'```{block_lang}')
                    result.extend([l for l in code_buffer if not l.strip().startswith('`')])
                    result.append('```')
                    in_code_block = False
                else:
                    if lang: block_lang = lang
        else:
            if in_code_block: code_buffer.append(line)
            else: result.append(line)
    
    if in_code_block:
        result.append(f'```{block_lang}')
        result.extend([l for l in code_buffer if not l.strip().startswith('`')])
        result.append('```')

    final = '\n'.join(result)
    return re.sub(r'```\w*\n\s*```\n?', '', final)

def fix_flattened_blocks(content):
    # Detect long lines in code blocks that should be multi-line
    def expand_block(match):
        lang = match.group(1)
        code = match.group(2)
        # Fix registry keys on one line
        if 'HKEY_' in code:
            code = re.sub(r'(\s+)(HKEY_[A-Z_]+\\)', r'\n\2', code)
        # Fix PowerShell commands separated by ;
        if lang == 'powershell' or '$' in code:
            if len(code) > 100 and ';' in code:
                code = code.replace(' ; ', ';\n').replace('; ', ';\n')
        return f'```{lang}\n{code.strip()}\n```'
    
    return re.sub(r'```(\w*)\n([\s\S]*?)\n```', expand_block, content)

def sanitize_content(content, args):
    # 1. Basic cleanups
    content = content.replace('\\_', '_')
    content = fix_mangled_paths(content)
    
    if args.upgrade_images:
        # 2. Convert WordPress [caption] shortcodes to Hugo {{< figure >}}
        def replace_caption(match):
            inner = match.group(1)
            img_match = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', inner, re.IGNORECASE)
            last_tag_end = inner.rfind('>')
            caption_text = inner[last_tag_end+1:].strip() if last_tag_end != -1 else ""
            
            if img_match:
                src = img_match.group(1)
                alt = img_match.group(2)
                
                clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', src, flags=re.IGNORECASE)
                filename = os.path.basename(clean_src)
                final_src = f"{args.image_dir}/{filename}"
                
                return f'{{{{< figure src="{final_src}" alt="{alt}" caption="{caption_text}" >}}}}'
            return inner

        content = re.sub(r'\[caption[^\]]*\]([\s\S]*?)\[/caption\]', replace_caption, content, flags=re.IGNORECASE)

        # 3. CONVERT MARKDOWN IMAGE LINKS TO FIGURES
        def replace_md_link_to_figure(match):
            alt = match.group(1).strip()
            thumb_src = match.group(2)
            orig_src = match.group(3)
            
            title_match = re.search(r'\s+"([^"]+)"', thumb_src)
            if not alt and title_match: alt = title_match.group(1)
                
            orig_src_clean = orig_src.split(' "')[0].split(" '")[0].strip()
            filename = os.path.basename(orig_src_clean)
            final_src = f"{args.image_dir}/{filename}"
            
            caption_attr = f' caption="{alt}"' if alt else ''
            return f'{{{{< figure src="{final_src}" alt="{alt}"{caption_attr} >}}}}'

        content = re.sub(r'\[\!\[(.*?)\]\((.*?)\)\]\((.*?)\)', replace_md_link_to_figure, content)

        # 4. CONVERT STANDALONE MARKDOWN IMAGES TO FIGURES
        def replace_md_img_to_figure(match):
            alt = match.group(1).strip()
            src = match.group(2)
            
            if '{{< figure' in match.group(0): return match.group(0)
                
            title_match = re.search(r'\s+"([^"]+)"', src)
            if not alt and title_match: alt = title_match.group(1)
                
            clean_src = src.split(' "')[0].split(" '")[0].strip()
            clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', clean_src, flags=re.IGNORECASE)
            filename = os.path.basename(clean_src)
            final_src = f"{args.image_dir}/{filename}"
            
            caption_attr = f' caption="{alt}"' if alt else ''
            return f'{{{{< figure src="{final_src}" alt="{alt}"{caption_attr} >}}}}'

        content = re.sub(r'(?<!\[)\!\[(.*?)\]\((.*?)\)', replace_md_img_to_figure, content)

        # 5. CONVERT ANY RAW <img> TAGS TO FIGURES
        def wrap_raw_img(match):
            html = match.group(0)
            src_match = re.search(r'src="([^"]+)"', html, re.IGNORECASE)
            alt_match = re.search(r'alt="([^"]*)"', html, re.IGNORECASE)
            if src_match:
                src = src_match.group(1)
                alt = alt_match.group(1) if alt_match else ""
                clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', src, flags=re.IGNORECASE)
                filename = os.path.basename(clean_src)
                final_src = f"{args.image_dir}/{filename}"
                return f'{{{{< figure src="{final_src}" alt="{alt}" >}}}}'
            return html

        content = re.sub(r'<a[^>]*>(<img[^>]+>)</a>', r'\1', content, flags=re.IGNORECASE)
        content = re.sub(r'<img[^>]+>', wrap_raw_img, content, flags=re.IGNORECASE)

    if args.add_lead:
        # 6. Wrap the first paragraph in the specified lead shortcode
        lead_open = f'{{{{< {args.lead_shortcode} >}}}}'
        lead_close = f'{{{{< /{args.lead_shortcode} >}}}}'
        if lead_open not in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith('---') and not line.startswith('#'):
                    lines[i] = f'{lead_open}\n{line}\n{lead_close}'
                    break
            content = '\n'.join(lines)

    if args.format_logs:
        # 7. Fence Technical Logs and Registry Keys (only if not already in a code block)
        parts = re.split(r'(```[\s\S]*?```|`[^`\n]+`)', content)
        for i in range(len(parts)):
            if not parts[i].startswith('`'):
                log_pattern = re.compile(r'((?:Event Type|Event Source|Event Category|Event ID|Description|ID)\s*:|HKLM\\|HKCU\\|HKEY_[A-Z_]+\\)([\s\S]*?)(?=\n\n|\n[A-Z][a-z]+ [A-Z]|(?:\n[A-Z][a-z]+){3,}|$)', re.IGNORECASE)
                def fence_log(match):
                    log_content = match.group(0).strip()
                    lang = detect_code_language(log_content)
                    return f'\n\n```{lang}\n{log_content}\n```\n'
                parts[i] = log_pattern.sub(fence_log, parts[i])
        content = ''.join(parts)

    if args.detect_code:
        # 8. Auto-detect language for existing code blocks
        def replace_code_lang(match):
            lang = match.group(1).lower()
            code = match.group(2)
            if lang in ['', 'text', 'none']:
                detected = detect_code_language(code)
                if detected != 'text': return f'```{detected}\n{code}\n```'
            return match.group(0)
        content = re.sub(r'```(\w*)\n([\s\S]*?)\n```', replace_code_lang, content)

    # 9. Final Cleanup Pass: Normalize fences and fix flattened blocks
    content = normalize_fences(content)
    content = fix_flattened_blocks(content)

    return content

def process_posts(directory, args):
    for root, dirs, files in os.walk(directory):
        if 'index.md' in files:
            file_path = os.path.join(root, 'index.md')
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            parts = content.split('---\n', 2)
            
            if len(parts) >= 3:
                front_matter_str = parts[1]
                body = parts[2]
                
                if args.update_front_matter:
                    try:
                        front_matter = yaml.safe_load(front_matter_str)
                        
                        if args.set_fm:
                            for kv in args.set_fm:
                                if '=' in kv:
                                    k, v = kv.split('=', 1)
                                    val_str = v.strip()
                                    if val_str.lower() in ('true', 'yes'):
                                        parsed_val = True
                                    elif val_str.lower() in ('false', 'no'):
                                        parsed_val = False
                                    else:
                                        try:
                                            parsed_val = int(val_str)
                                        except ValueError:
                                            try:
                                                parsed_val = float(val_str)
                                            except ValueError:
                                                parsed_val = val_str
                                    front_matter[k.strip()] = parsed_val
                        
                        ordered_keys = args.fm_order
                        ordered_fm = {}
                        for k in ordered_keys:
                            if k in front_matter:
                                ordered_fm[k] = front_matter[k]
                        for k in front_matter:
                            if k not in ordered_keys:
                                ordered_fm[k] = front_matter[k]
                                
                        front_matter_str = yaml.dump(ordered_fm, sort_keys=False)
                    except Exception as e:
                        print(f"Error parsing front matter in {file_path}: {e}")
                
                new_body = sanitize_content(body, args)
                
                # If front matter was not updated, front_matter_str retains its exact original string formatting.
                new_content = '---\n' + front_matter_str + '---\n' + new_body
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Supplemental utility to sanitize and enhance Markdown exports for Hugo.")
    parser.add_argument('directory', nargs='?', default='content/posts', help='Target directory to process.')
    parser.add_argument('--upgrade-images', action='store_true', help='Convert images to Hugo figure shortcodes.')
    parser.add_argument('--image-dir', default='images', help='Subdirectory for images in page bundles (default: images).')
    parser.add_argument('--add-lead', action='store_true', help='Wrap the first paragraph in a lead shortcode.')
    parser.add_argument('--lead-shortcode', default='lead', help='Shortcode name to use for the lead paragraph (default: lead).')
    parser.add_argument('--format-logs', action='store_true', help='Fence technical logs and registry keys.')
    parser.add_argument('--detect-code', action='store_true', help='Auto-detect language for generic code blocks.')

    parser.add_argument('--update-front-matter', action='store_true', help='Update YAML front matter and reorder keys.')
    parser.add_argument('--set-fm', nargs='+', help='Key=Value pairs to add/update in front matter (e.g., draft=False showTableOfContents=True).', default=[])
    parser.add_argument('--fm-order', nargs='+', help='Preferred order of front matter keys.', default=['title', 'date', 'categories', 'tags'])
    parser.add_argument('--all', action='store_true', help='Enable all sanitization features (for fresh exports).')
    
    args = parser.parse_args()
    
    if args.all:
        args.upgrade_images = True
        args.add_lead = True
        args.format_logs = True
        args.detect_code = True
        args.update_front_matter = True
        # Provide some sensible defaults for an 'all' run if set_fm wasn't provided
        if not args.set_fm:
            args.set_fm = ['draft=False', 'showTableOfContents=True']
        if args.fm_order == ['title', 'date', 'categories', 'tags']:
            args.fm_order = ['title', 'date', 'categories', 'tags', 'showTableOfContents', 'draft']
            
    process_posts(args.directory, args)