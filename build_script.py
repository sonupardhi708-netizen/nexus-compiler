import os, requests

# API credentials
key = os.getenv('GROQ_API_KEY', '').strip().replace('"', '').replace("'", "")
prmt = os.getenv('APP_PROMPT', 'Simple dashboard app')

if not key:
    print("API Key missing!"); exit(1)

# API target setup
t_path = "./project_source/lib/main.dart"
url = "https://api.groq.com/openai/v1/chat/completions"
h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

# Payload building
sys_msg = "Act as expert Flutter Developer. Output ONLY valid, complete Dart code. Wrap your code inside a markdown block starting with ```dart and ending with 
```. No text before or after."
data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": prmt}
    ],
    "temperature": 0.2
}

try:
    print("🤖 Fetching from Groq...")
    r = requests.post(url, headers=h, json=data)
    txt = r.json()['choices'][0]['message']['content'].strip()
    
    # Safe splitting without broken lines
    clean = txt.split("```dart")[1].split("```")[0].strip() if "```dart" in txt else txt.strip()
    
    os.makedirs(os.path.dirname(t_path), exist_ok=True)
    with open(t_path, "w") as f:
        f.write(clean)
    print("🚀 Deployed successfully!")
except Exception as e:
    print(f"❌ Error: {e}")
