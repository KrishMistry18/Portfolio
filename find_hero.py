f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
lines = f.splitlines()
for i, line in enumerate(lines):
    if '<header class="hero">' in line:
        print(f'Hero starts at line {i+1}')
        break
