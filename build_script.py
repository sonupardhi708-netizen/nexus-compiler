import os, requests
p = os.getenv('APP_PROMPT', 'Premium App')
k = os.getenv('GROQ_API_KEY', '').strip().replace('*', '')

# कीपैड सुरक्षा: यूआरएल को टुकड़ों में जोड़ दिया, अब कीपैड डबल नहीं कर पाएगा
u = "https://api." + "groq.com/openai/v1/chat/completions"
w = "".join(["B", "e", "a", "r", "e", "r"])
h = {"Authorization": f"{w} {k}", "Content-Type": "application/json"}

s = "You are an expert Flutter developer. Output ONLY valid ready-to-run Dart code starting directly with imports. Never include markdown blocks like ```dart or descriptions. Full code only."
b = {"model": "llama3-70b-8192", "messages": [{"role": "system", "content": s}, {"role": "user", "content": p}], "temperature": 0.1}

try:
    print("AI Status: Fetching fresh code...")
    r = requests.post(u, json=b, headers=h).json()
    raw = r['choices'][0]['message']['content'].strip()
    
    if "import" in raw:
        raw = "import" + raw.split("import", 1)[1]
    if "`" in raw:
        raw = raw.split("`")[0].strip()
        
    t = 'lib/main.dart'
    if os.path.exists(t): os.remove(t)
    os.makedirs('lib', exist_ok=True)
    
    f = open(t, 'w', encoding='utf-8')
    f.write(raw)
    f.close()
    print("Success: Fresh Dart code saved safely!")
except Exception as e:
    print(f"Build Error: {e}")
