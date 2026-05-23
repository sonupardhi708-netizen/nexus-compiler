import os, requests

api_key = os.getenv('GROQ_API_KEY', '').strip().replace('"', '').replace("'", "")
prompt = os.getenv('APP_PROMPT', 'Simple dashboard app')

if not api_key:
    print("API Key missing!"); exit(1)

# सीधे गिटहब एनवायरनमेंट में main.dart का पाथ सेट करना
target_path = "./project_source/lib/main.dart"

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "Act as expert Flutter Developer. Output ONLY valid Dart code starting with import. No markdown block, no code blocks, no explanations, just raw dart code."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

try:
    print("🤖 Agent: Fetching raw code from Groq...")
    res = requests.post(url, headers=headers, json=data)
    clean_code = res.json()['choices'][0]['message']['content'].strip()
    
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w") as f:
        f.write(clean_code)
    print(f"🚀 Successfully deployed to {target_path}")
except Exception as e:
    print(f"❌ Error: {e}")
