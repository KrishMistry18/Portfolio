import re
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
print(re.findall(r'<section id="([^"]+)"', f))
