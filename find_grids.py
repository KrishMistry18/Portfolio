import re
f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()

live = re.search(r'<section\s+id="live-status"[^>]*>.*?</section>', f, re.DOTALL)
if live:
    print('Live Status classes:', re.findall(r'class="([^"]*grid[^"]*)"', live.group(0)))
else:
    print('No live-status section')

proj = re.search(r'<section\s+id="projects"[^>]*>.*?</section>', f, re.DOTALL)
if proj:
    print('Projects classes:', re.findall(r'class="([^"]*grid[^"]*)"', proj.group(0)))
else:
    print('No projects section')
