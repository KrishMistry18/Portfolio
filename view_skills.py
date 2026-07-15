import re
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
match = re.search(r'<section id="skills"[^>]*>.*?</section>', f, re.DOTALL)
if match: print(match.group(0)[:500])
