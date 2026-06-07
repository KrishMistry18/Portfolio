import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Update projects
    projects = ['AyurWell.png', 'EduCycle.png', 'Nexus.png', 'WatchParty.png', 
                'chessanalyzer.png', 'hemisphere.png', 'heritageguide.png', 'impactglobe.png']
    for p in projects:
        html = html.replace(f'"{p}"', f'"assets/projects/{p}"')
        html = html.replace(f"'{p}'", f"'assets/projects/{p}'")

    # Update certificates
    certs = ['Colloquium_certificate.jpg', 'Prayas_certificate.jpg', 'Volunteering_Colloquium_certificate.jpg',
             'BotCampusAI_certificate.jpg', 'Devtown_NoSQL_GDG.png', 'Devtown_NoSQL_MSIT.png', 
             'Devtown_NoSQL_Participation.png', 'WebAuth_GDG_certificate.jpg', 'WebAuth_MSIT_certificate.jpg',
             'WebAuth_Participation_certificate.jpg', 'gemini_game_night_certificate.jpg',
             'Colloquium_2026_certificate.jpg', 'AIquiz_student_ambassador_certificate.jpg',
             'NSS_HEAD_Certificate.jpg', 'Devtown_ML_GDG.jpg', 'Devtown_ML_MSIT.jpg', 'Devtown_ML_Participation.jpg']
    for c in certs:
        html = html.replace(f'"{c}"', f'"assets/certificates/{c}"')
        html = html.replace(f"'{c}'", f"'assets/certificates/{c}'")

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
update_html()
print("Paths updated.")
