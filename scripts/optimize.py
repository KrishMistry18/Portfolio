import os
import re
import urllib.parse

html_file = 'index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_dir = 'assets/Experience & Competitions'
new_dir = 'assets/experience'

if os.path.exists(old_dir):
    os.rename(old_dir, new_dir)

def kebab_case(filename):
    return filename.lower().replace(' ', '-')

# Find all occurrences
def replacer(match):
    encoded_filename = match.group(1)
    filename = urllib.parse.unquote(encoded_filename)
    new_filename = kebab_case(filename)
    
    # rename on disk if it exists
    old_path = os.path.join(new_dir, filename)
    new_path = os.path.join(new_dir, new_filename)
    if os.path.exists(old_path) and old_path != new_path:
        os.rename(old_path, new_path)
        
    return f"assets/experience/{new_filename}"

new_html = re.sub(r'assets/Experience(?:%20| )&(?:%20| )Competitions/([^"\'\?]+)', replacer, html)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Optimization complete.")
