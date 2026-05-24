import os
import requests

p = os.getenv('APP_PROMPT', 'Premium App')
k = os.getenv('GROQ_API_KEY', '').strip().replace('*', '')
u = "https://api.groq.com/openai/v1/chat/completions"

# कीपैड सुरक्षा: 'Bearer' शब्द ही गायब कर दिया, अब कीपैड कुछ नहीं बिगाड़ पाएगा!
word = "".join(["B", "e", "a", "r", "e", "r"])
h = {"Authorization": f"{word} {k}", "Content-Type": "application/json"}

s = "You are an expert Flutter developer. Generate ONLY complete, production-ready Flutter app code. Start directly with imports. No markdown blocks, no explanations."
b = {"model": "llama3-70b-8192", "messages": [{"role": "system", "content": s}, {"role": "user", "content": p}], "temperature": 0.2}

try:
    print("Fetching clean code...")
    r = requests.post(u, headers=h, json=b).json()
    raw = r['choices'][0]['message']['content'].strip()
    
    if "import" in raw:
        raw = "import" + raw.split("import", 1)[1]
    if "void main" in raw and not raw.startswith("import"):
        raw = "void main" + raw.split("void main", 1)[1]
        
    os.makedirs('lib', exist_ok=True)
    
    # कीपैड सुरक्षा: 'with open' का झंझट ही खत्म, बड़े 'With' का कोई एरर नहीं आएगा!
    f = open('lib/main.dart', 'w', encoding='utf-8')
    f.write(raw)
    f.close()
        
    print("Success: Pure Dart code saved to lib/main.dart")
except Exception as e:
    print(f"Build Error: {e}")
  
