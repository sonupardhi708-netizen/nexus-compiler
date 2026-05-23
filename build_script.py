import os, requests

api_key = os.getenv('GROQ_API_KEY', '').strip().replace('"', '').replace("'", "")
prompt = os.getenv('APP_PROMPT', 'Simple dashboard app')

if not api_key:
    print("API Key is missing!")
    exit(1)

main_paths = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f == "main.dart":
            main_paths.append(os.path.join(root, f))

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "Act as expert Flutter Developer. Output ONLY valid Dart code inside a markdown block starting with ```dart. No explanations."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

try:
    res = requests.post(url, headers=headers, json=data)
    ai_text = res.json()['choices'][0]['message']['content']
    
    if "
```dart" in ai_text:
        clean_code = ai_text.split("```dart")[1].split("```")[0].strip()
    else:
        clean_code = ai_text.strip()

    if main_paths:
        for path in main_paths:
            with open(path, "w") as f:
                f.write(clean_code)
            print(f"Deployed to: {path}")
    else:
        os.makedirs("project_source/lib", exist_ok=True)
        with open("project_source/lib/main.dart", "w") as f:
            f.write(clean_code)
        print("Deployed to default path.")

except Exception as e:
    print(f"Error: {e}")
