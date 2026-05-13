import os
import re
import yaml
import argparse

def sanitize_content(content, args):
    # 1. Fix escaped underscores common in WordPress exports
    content = content.replace('\\_', '_')
    
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
                final_src = f"images/{filename}"
                
                return f'{{{{< figure src="{final_src}" alt="{alt}" caption="{caption_text}" >}}}}'
            return inner

        content = re.sub(r'\[caption[^\]]*\]([\s\S]*?)\[/caption\]', replace_caption, content, flags=re.IGNORECASE)

        # 3. CONVERT MARKDOWN IMAGE LINKS TO FIGURES
        def replace_md_link_to_figure(match):
            alt = match.group(1).strip()
            thumb_src = match.group(2)
            orig_src = match.group(3)
            
            # If alt is empty, try to extract it from the title attribute
            title_match = re.search(r'\s+"([^"]+)"', thumb_src)
            if not alt and title_match:
                alt = title_match.group(1)
                
            # Clean up orig_src in case it has a title
            orig_src_clean = orig_src.split(' "')[0].split(" '")[0].strip()
            filename = os.path.basename(orig_src_clean)
            final_src = f"images/{filename}"
            
            caption_attr = f' caption="{alt}"' if alt else ''
            return f'{{{{< figure src="{final_src}" alt="{alt}"{caption_attr} >}}}}'

        content = re.sub(r'\[\!\[(.*?)\]\((.*?)\)\]\((.*?)\)', replace_md_link_to_figure, content)

        # 4. CONVERT STANDALONE MARKDOWN IMAGES TO FIGURES
        def replace_md_img_to_figure(match):
            alt = match.group(1).strip()
            src = match.group(2)
            
            if '{{< figure' in match.group(0):
                return match.group(0)
                
            title_match = re.search(r'\s+"([^"]+)"', src)
            if not alt and title_match:
                alt = title_match.group(1)
                
            clean_src = src.split(' "')[0].split(" '")[0].strip()
            clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', clean_src, flags=re.IGNORECASE)
            filename = os.path.basename(clean_src)
            final_src = f"images/{filename}"
            
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
                final_src = f"images/{filename}"
                return f'{{{{< figure src="{final_src}" alt="{alt}" >}}}}'
            return html

        content = re.sub(r'<a[^>]*>(<img[^>]+>)</a>', r'\1', content, flags=re.IGNORECASE)
        content = re.sub(r'<img[^>]+>', wrap_raw_img, content, flags=re.IGNORECASE)

    if args.add_lead:
        # 6. Wrap the first paragraph in {{< lead >}} if it's not already
        if '{{< lead >}}' not in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith('---') and not line.startswith('#'):
                    lines[i] = f'{{{{< lead >}}}}\n{line}\n{{{{< /lead >}}}}'
                    break
            content = '\n'.join(lines)

    if args.format_logs:
        # 7. Fence Technical Logs and Registry Keys
        log_pattern = re.compile(r'(HKLM\\|HKCU\\|HKEY_[A-Z_]+\\|Event ID\s*:|ID\s*:\s*\d+)([\s\S]*?)(?=\n\n|\n[A-Z]|$)', re.IGNORECASE)
        def fence_log(match):
            log_content = match.group(0).strip()
            return f'```text\n{log_content}\n```'
        
        content = log_pattern.sub(fence_log, content)


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
                        front_matter['draft'] = False
                        front_matter['showTableOfContents'] = True
                        
                        ordered_keys = ['title', 'date', 'categories', 'showTableOfContents', 'draft']
                        ordered_fm = {}
                        for k in ordered_keys:
                            if k in front_matter:
                                ordered_fm[k] = front_matter[k]
                        for k in front_matter:
                            if k not in ordered_keys:
                                ordered_fm[k] = front_matter[k]
                                
                        front_matter_str = yaml.dump(ordered_fm, sort_keys=False)
                    except Exception:
                        pass
                
                new_body = sanitize_content(body, args)
                
                # If front matter was not updated, front_matter_str retains its exact original string formatting.
                new_content = '---\n' + front_matter_str + '---\n' + new_body
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Supplemental tool to sanitize WordPress markdown exports.")
    parser.add_argument('directory', nargs='?', default='content/posts', help='Target directory to process.')
    parser.add_argument('--upgrade-images', action='store_true', help='Convert images to Hugo figure shortcodes.')
    parser.add_argument('--add-lead', action='store_true', help='Wrap the first paragraph in {{< lead >}} shortcodes.')
    parser.add_argument('--format-logs', action='store_true', help='Fence technical logs and registry keys.')

    parser.add_argument('--update-front-matter', action='store_true', help='Update YAML front matter (draft, toc) and reorder keys.')
    parser.add_argument('--all', action='store_true', help='Enable all sanitization features (for fresh exports).')
    
    args = parser.parse_args()
    
    if args.all:
        args.upgrade_images = True
        args.add_lead = True
        args.format_logs = True
        args.update_front_matter = True
        
    process_posts(args.directory, args)