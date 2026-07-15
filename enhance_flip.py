import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

f = open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', encoding='utf-8').read()

# Increase height of flip card and add overflow to back face
f = re.sub(r'(\.proj-flip-card\s*\{[^}]*height:\s*)300px(;\s*\})', r'\g<1>480px\g<2>', f)
f = re.sub(r'(\.proj-flip-back\s*\{[^}]*)(\})', r'\g<1>overflow-y: auto;\n                \g<2>', f)

# Add new CSS classes
new_css = """
                .proj-flip-back-points {
                    padding-left: 1rem;
                    margin-bottom: 0.8rem;
                    font-size: 0.85rem;
                    color: var(--text-muted);
                    line-height: 1.4;
                }
                .proj-flip-back-points li {
                    margin-bottom: 0.3rem;
                }
                .proj-flip-back-tech {
                    background: rgba(255,255,255,0.03);
                    border-radius: 6px;
                    padding: 0.8rem;
                    margin-bottom: 1rem;
                    border: 1px solid var(--border);
                }
                .proj-flip-back-tech h4 {
                    font-family: 'DM Mono', monospace;
                    font-size: 0.75rem;
                    color: var(--text-secondary);
                    margin-bottom: 0.4rem;
                    text-transform: uppercase;
                    letter-spacing: 0.05em;
                    margin-top: 0;
                }
                .proj-flip-back-tech p {
                    font-size: 0.8rem;
                    color: var(--text-muted);
                    line-height: 1.4;
                    margin: 0;
                }
"""

css_insert_point = r'(\.proj-flip-back-title\s*\{.*?\}\s*)'
f = re.sub(css_insert_point, r'\g<1>' + new_css.strip() + '\n                ', f, count=1)


cards_data = {
    "ChessAnalyzer": {
        "points": [
            "Play-vs-Stockfish with adjustable strength, multi-engine support with WASM threads gracefully degrading based on CPU.",
            "Move classification, multi-PV engine lines, and game summaries highlighting inaccuracies, mistakes, and blunders.",
            "40+ piece themes, SAN move list, zero backend dependency for analysis."
        ],
        "tech": "The biggest challenge was running a heavy C++ chess engine in JS without freezing the UI. I compiled Stockfish to WebAssembly (WASM) and ran it inside Web Workers, communicating via message passing.",
    },
    "HeritageGuide": {
        "points": [
            "Dynamic map integration using Leaflet and OpenStreetMap for accurate site discovery.",
            "Built a full-stack Django architecture handling secure slot booking, authentication, and routing.",
            "Firebase-backed features ensure real-time data flow for peak hour updates and reviews."
        ],
        "tech": "The routing engine needed to be fast and multimodal. Instead of building from scratch, I integrated with OpenRouteService APIs but cached frequent routes in Redis to minimize API costs and latency.",
    },
    "EduCycle": {
        "points": [
            "Integrated Stripe for secure, verified student-to-student transactions.",
            "Developed a robust PWA architecture enabling students to browse and message offline on campus.",
            "Utilized Redis caching to serve the marketplace feed in under 100ms."
        ],
        "tech": "Managing real-time P2P chat alongside transactional data required careful planning. I decoupled the chat microservice using WebSockets while Django handles heavy DB relations.",
    },
    "AyurWell": {
        "points": [
            "Formulated an intricate scoring algorithm mapping user survey inputs to precise Ayurvedic Dosha profiles.",
            "Integrated LLMs to dynamically generate highly personalized, season-aware dietary plans.",
            "Constructed a fluid dashboard using Recharts to visualize wellness progress over time."
        ],
        "tech": "Feeding complex health profiles into the LLM safely was critical. I implemented a strict prompt chaining pipeline with validation layers to ensure the AI generated safe advice.",
    },
    "WatchParty": {
        "points": [
            "Engineered a custom WebRTC signaling server using Socket.IO to establish low-latency peer connections.",
            "Implemented robust timestamp synchronization algorithms to ensure sub-second video playback alignment.",
            "Built lightweight, zero-install architecture focusing on pure client-side P2P media flow."
        ],
        "tech": "Instead of relaying video through a central server (expensive and slow), I forced a pure P2P mesh network for smaller rooms. The signaling server purely orchestrates connections.",
    },
    "Nexus Financial": {
        "points": [
            "Architected a double-entry ledger system in Java to guarantee atomic, ACID-compliant transactions.",
            "Enforced strict security measures using JDBC prepared statements to prevent any SQL injection vulnerabilities.",
            "Developed a comprehensive dual-table audit trail to track every single balance change and user action."
        ],
        "tech": "Ensuring transaction atomicity during concurrent ATM operations was paramount. I heavily utilized MySQL row-level locking (SELECT ... FOR UPDATE) to prevent race conditions.",
    }
}

for title, data in cards_data.items():
    points_html = "".join([f"<li>{p}</li>" for p in data['points']])
    replacement_content = f"""
                            <ul class="proj-flip-back-points">
                                {points_html}
                            </ul>
                            <div class="proj-flip-back-tech">
                                <h4>⚙️ Hardest Technical Decision</h4>
                                <p>{data['tech']}</p>
                            </div>
    """
    
    # We find the back face block for this specific card title
    pattern = rf'(<div class="proj-flip-back-title">{title}</div>)\s*<p class="d">.*?</p>'
    f = re.sub(pattern, rf'\g<1>{replacement_content}', f, flags=re.DOTALL)

with open('c:/Users/Admin/Desktop/Krish/Projects/Portfolio/index.html', 'w', encoding='utf-8') as file:
    file.write(f)

print("Flip cards enhanced successfully!")
