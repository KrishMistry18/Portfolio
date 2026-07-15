import sys
sys.stdout.reconfigure(encoding='utf-8')
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
import re
match = re.search(r'<div class="proj-flip-grid".*?</section>', f, re.DOTALL)
if match:
    with open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/projects_html.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(0))
