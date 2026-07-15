f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()
print('ChessAnalyzer card in flip grid:', 'ChessAnalyzer' in f.split('<div class="proj-flip-grid">')[-1])
print('HeritageGuide card in flip grid:', 'HeritageGuide' in f.split('<div class="proj-flip-grid">')[-1])
print('Hardest Technical Decision added:', '⚙️ Hardest Technical Decision' in f)
