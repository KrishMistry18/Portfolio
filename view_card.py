import re
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
match = re.search(r'<div class="proj-flip-card"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>', f, re.DOTALL)
if match: print(match.group(0))
