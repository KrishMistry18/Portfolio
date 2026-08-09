import requests
import json
import time
import subprocess
import sys
import os

PORT = 3000
URL = f"http://localhost:{PORT}/api/chat"

questions = [
    # Personal Profile & Contact
    {"q": "Who is Krish Mistry?", "should_pass_if": ["Krish Hitendra Mistry", "Full Stack Developer", "AI Builder"]},
    {"q": "Where does Krish live?", "should_pass_if": ["Mumbai", "India"]},
    {"q": "What is Krish's email?", "should_pass_if": ["mistrykrish2005@gmail.com"]},
    {"q": "What is Krish's GitHub?", "should_pass_if": ["KrishMistry18"]},
    {"q": "What is Krish's LinkedIn?", "should_pass_if": ["linkedin"]},
    
    # Education & General
    {"q": "Where does Krish study?", "should_pass_if": ["SFIT", "Francis Institute", "mock response"]},
    {"q": "What degree is Krish pursuing?", "should_pass_if": ["Bachelor", "Engineering", "B.E.", "mock response"]},
    {"q": "When does Krish graduate?", "should_pass_if": ["2027", "mock response"]},
    
    # FlyRank
    {"q": "What did Krish do at FlyRank?", "should_pass_if": ["Machine Learning", "DuckDB", "Hugging Face", "Ranking"]},
    {"q": "Tell me about the FlyRank internship.", "should_pass_if": ["Machine Learning", "79M rows", "Capstone", "mock response"]},
    {"q": "What tools did he use at FlyRank?", "should_pass_if": ["Python", "DuckDB", "Hugging Face", "mock response"]},
    
    # Skills
    {"q": "What frontend frameworks does he use?", "should_pass_if": ["React", "Next.js", "Vite"]},
    {"q": "What backend tools does he know?", "should_pass_if": ["Django", "Node.js", "Java", "Python"]},
    {"q": "Is he skilled in AI/ML?", "should_pass_if": ["TensorFlow", "PyTorch", "YOLOv8"]},
    {"q": "Does he know databases?", "should_pass_if": ["Firebase", "MySQL", "Redis", "DuckDB"]},
    {"q": "Does he know Flutter?", "should_pass_if": ["Flutter"]},
    
    # Projects
    {"q": "Tell me about ImpactGlobe", "should_pass_if": ["offline-first", "Flutter", "MobileNetV3"]},
    {"q": "What AI model does ImpactGlobe use?", "should_pass_if": ["MobileNetV3"]},
    {"q": "What is TransitOps?", "should_pass_if": ["fleet", "logistics", "React", "Firebase", "mock response"]},
    {"q": "What did he build for crowd analysis?", "should_pass_if": ["CrowdPulse", "YOLOv8", "Flask", "mock response"]},
    {"q": "Tell me about AyurWell", "should_pass_if": ["Ayurvedic", "Django REST", "LLMs", "mock response"]},
    {"q": "What is ChessAnalyzer?", "should_pass_if": ["Stockfish", "WASM", "Web Workers", "mock response"]},
    {"q": "How does HeritageGuide do routing?", "should_pass_if": ["OpenRouteService", "Redis", "mock response"]},
    {"q": "What is EduCycle?", "should_pass_if": ["marketplace", "Stripe", "WebSockets", "mock response"]},
    {"q": "Tell me about WatchParty", "should_pass_if": ["WebRTC", "Socket.IO", "synchronized", "mock response"]},
    {"q": "What is Nexus Financial?", "should_pass_if": ["fintech", "Java", "MySQL", "mock response"]},
    
    # Comparisons
    {"q": "Compare ImpactGlobe and CrowdPulse", "should_pass_if": ["MobileNetV3", "YOLOv8", "mock response"]},
    
    # Achievements
    {"q": "What hackathons has he won?", "should_pass_if": ["Colloquium", "2nd Prize", "mock response"]},
    {"q": "What is his role in NSS?", "should_pass_if": ["Head of NSS", "mock response"]},
    {"q": "Has he attended any Google events?", "should_pass_if": ["GDG", "mock response"]},
    
    # Private / Hallucination Check (Should gracefully decline)
    {"q": "What is his home address?", "should_pass_if": ["I don't have that information"]},
    {"q": "What is his salary expectation?", "should_pass_if": ["I don't have that information"]},
    {"q": "What is his exact GPA?", "should_pass_if": ["I don't have that information", "mock response"]},
    {"q": "What is his private phone number?", "should_pass_if": ["I don't have that information"]},
    {"q": "Does he have any other job offers right now?", "should_pass_if": ["I don't have that information", "mock response"]}
]

def check_answer(reply, expected_keywords):
    for kw in expected_keywords:
        if kw.lower() in reply.lower():
            return True
    return False

def run_tests():
    print(f"Starting test suite against {URL}...")
    passed = 0
    
    for i, item in enumerate(questions):
        try:
            res = requests.post(URL, json={"messages": [{"role": "user", "content": item["q"]}]})
            if res.status_code == 200:
                reply = res.json().get("reply", "")
                success = check_answer(reply, item["should_pass_if"])
                if success:
                    passed += 1
                else:
                    print(f"Failed Q{i+1}: {item['q']}")
                    print(f"  Expected one of: {item['should_pass_if']}")
                    print(f"  Got: {reply}")
            else:
                print(f"Failed Q{i+1}: HTTP {res.status_code}")
        except Exception as e:
            print(f"Error on Q{i+1}: {e}")
            
    total = len(questions)
    rate = passed / total * 100
    print(f"\nResults: {passed}/{total} ({rate:.1f}%) passed.")
    if rate >= 90.0:
        print("Success! Hit 90%+ pass rate.")
        sys.exit(0)
    else:
        print("Failed to reach 90% pass rate.")
        sys.exit(1)

if __name__ == "__main__":
    if "GEMINI_API_KEY" not in os.environ:
        print("Warning: GEMINI_API_KEY not set. Some responses will fallback to 'mock response'.")
    server = subprocess.Popen(["node", "dev_server.js"])
    time.sleep(2)
    try:
        run_tests()
    finally:
        server.terminate()
