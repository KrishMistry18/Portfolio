import os

filepath = r'c:\Users\Admin\Desktop\Krish\Projects\Portfolio\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_style = False
in_custom_cursor_script = False
style_count = 0
for i, line in enumerate(lines):
    if '<style>' in line:
        style_count += 1
        if style_count == 1:
            new_lines.append('<link rel="stylesheet" href="style.css">\n')
        in_style = True
        continue
    
    if '</style>' in line:
        in_style = False
        continue
        
    if '<script>' in line and i+1 < len(lines) and 'const customCursor' in lines[i+1]:
        in_custom_cursor_script = True
        continue
        
    if in_custom_cursor_script and '</script>' in line:
        in_custom_cursor_script = False
        continue
        
    if not in_style and not in_custom_cursor_script:
        if 'id="custom-cursor"' in line or '<!-- Custom Dynamic Cursor -->' in line:
            continue
        new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print('Done!')
