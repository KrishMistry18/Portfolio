import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
match = re.search(r'<div class="proj-flip-face proj-flip-front">.*?</div>', f, re.DOTALL)
if match: print(match.group(0))
