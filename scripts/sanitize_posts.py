import os
import re
import yaml

def sanitize_content(content):
    # 1. Fix escaped underscores common in WordPress exports
    content = content.replace('\\_', '_')
    
    # 2. Convert WordPress [caption] shortcodes to Hugo {{< figure >}}
    # These might already be in Markdown form if Turndown was used, but let's handle both
    def replace_caption(match):
        inner = match.group(1)
        img_match = re.search(r'<img[^>]*src="([^"]+)"[^>]*alt="([^"]*)"[^>]*>', inner, re.IGNORECASE)
        # The caption is usually the text after the last tag
        last_tag_end = inner.rfind('>')
        caption_text = inner[last_tag_end+1:].strip() if last_tag_end != -1 else ""
        
        if img_match:
            src = img_match.group(1)
            alt = img_match.group(2)
            
            # Clean the src: remove resolution suffixes and point to local images/ folder
            clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', src, flags=re.IGNORECASE)
            filename = os.path.basename(clean_src)
            final_src = f"images/{filename}"
            
            return f'{{{{< figure src="{final_src}" alt="{alt}" caption="{caption_text}" >}}}}'
        return inner

    content = re.sub(r'\[caption[^\]]*\]([\s\S]*?)\[/caption\]', replace_caption, content, flags=re.IGNORECASE)

    # 3. CONVERT MARKDOWN IMAGE LINKS TO FIGURES (The "Shadowbox" Fix)
    # This handles the pattern: [![alt](thumbnail)](original)
    def replace_md_link_to_figure(match):
        alt = match.group(1)
        thumb_src = match.group(2)
        orig_src = match.group(3)
        
        # We always want the original, cleanest filename
        filename = os.path.basename(orig_src)
        # Ensure it's pointing to our local images folder
        final_src = f"images/{filename}"
        
        return f'{{{{< figure src="{final_src}" alt="{alt}" >}}}}'

    # Pattern: [![Alt Text](images/thumb.png)](images/original.png)
    content = re.sub(r'\[\!\[([^\]]*)\]\(([^\)]+)\)\]\(([^\)]+)\)', replace_md_link_to_figure, content)

    # 4. CONVERT STANDALONE MARKDOWN IMAGES TO FIGURES
    # Pattern: ![Alt Text](images/img.png)
    def replace_md_img_to_figure(match):
        alt = match.group(1)
        src = match.group(2)
        
        # Skip if it was already turned into a figure
        if '{{< figure' in match.group(0):
            return match.group(0)
            
        # Clean resolution suffixes if any
        clean_src = re.sub(r'-\d+x\d+(\.[a-z]+)$', r'\1', src, flags=re.IGNORECASE)
        filename = os.path.basename(clean_src)
        final_src = f"images/{filename}"
        
        return f'{{{{< figure src="{final_src}" alt="{alt}" >}}}}'

    content = re.sub(r'(?<!\[)\!\[([^\]]*)\]\(([^\)]+)\)', replace_md_img_to_figure, content)

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

    # First strip <a> wrappers around raw <img>
    content = re.sub(r'<a[^>]*>(<img[^>]+>)</a>', r'\1', content, flags=re.IGNORECASE)
    # Then convert <img> to figure
    content = re.sub(r'<img[^>]+>', wrap_raw_img, content, flags=re.IGNORECASE)

    # 6. Wrap the first paragraph in {{< lead >}} if it's not already
    if '{{< lead >}}' not in content:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            # Skip empty lines, frontmatter, and headings
            if line.strip() and not line.startswith('---') and not line.startswith('#'):
                lines[i] = f'{{{{< lead >}}}}\n{line}\n{{{{< /lead >}}}}'
                break
        content = '\n'.join(lines)

    # 7. Fence Technical Logs and Registry Keys
    log_pattern = re.compile(r'(HKLM\\|HKCU\\|HKEY_[A-Z_]+\\|Event ID\s*:|ID\s*:\s*\d+)([\s\S]*?)(?=\n\n|\n[A-Z]|$)', re.IGNORECASE)
    def fence_log(match):
        log_content = match.group(0).strip()
        return f'```text\n{log_content}\n```'
    
    if '```' not in content:
        content = log_pattern.sub(fence_log, content)

    # 8. Remove Legacy Signatures
    content = re.sub(r'\n+Enjoy!\s*$', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\n+Ilan\s*$', '', content, flags=re.IGNORECASE)

    return content

def process_posts(directory):
    for root, dirs, files in os.walk(directory):
        if 'index.md' in files:
            file_path = os.path.join(root, 'index.md')
            with open(file_path, 'r') as f:
                content = f.read()
            
            parts = content.split('---\n', 2)
            
            if len(parts) >= 3:
                try:
                    front_matter = yaml.safe_load(parts[1])
                except Exception:
                    continue
                    
                body = parts[2]
                
                # Update Front Matter
                front_matter['draft'] = False
                front_matter['showTableOfContents'] = True
                
                # Sanitize Body
                new_body = sanitize_content(body)
                
                # Reconstruct
                new_content = '---\n' + yaml.dump(front_matter) + '---\n' + new_body
                
                with open(file_path, 'w') as f:
                    f.write(new_content)
                print(f"Upgraded: {file_path}")

if __name__ == "__main__":
    process_posts('content/posts')