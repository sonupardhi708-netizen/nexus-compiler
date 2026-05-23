import os, requests

api_key = os.getenv('GROQ_API_KEY', '').strip().replace('"', '').replace("'", "")
prompt = os.getenv('APP_PROMPT', 'Simple dashboard app')

if not api_key:
    print("API Key is missing!")
    exit(1)

url = "https://api.groq.com/openai/v1/chat/completions"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": "Act as an expert Flutter Developer. Output ONLY valid, clean Dart code inside a single markdown block. No explanations."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

try:
    res = requests.post(url, headers=headers, json=data)
    ai_text = res.json()['choices'][0]['message']['content']
    clean_code = ai_text.split("```")[1].replace("dart", "").strip() if "```" in ai_text else ai_text.strip()
    
    with open("project_source/lib/main.dart", "w") as f:
        f.write(clean_code)
    print("Code generated successfully!")
except Exception as e:
    print(f"Error occurred: {e}")
