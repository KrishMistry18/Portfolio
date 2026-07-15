import sys
sys.stdout.reconfigure(encoding='utf-8')
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
import re
match = re.search(r'<span class="proj-flip-front-name">Nexus.*?</span>.*?(?=<div class="proj-flip-face proj-flip-back">)', f, re.DOTALL)
if match: print(match.group(0))
