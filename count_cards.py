import re
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
print(len(re.findall(r'<div class="proj-flip-card', f)))
