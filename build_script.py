import os, requests, json, re
api_key = os.getenv('GROQ_API_KEY')
prompt = os.getenv('APP_PROMPT')

sys_ins = "Act as an expert Flutter Developer. Output ONLY valid, clean Dart code inside a single ```dart 
``` block. No explanations."
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
data = {"model": "llama3-70b-8192", "messages": [{"role": "system", "content": sys_ins}, {"role": "user", "content": prompt}], "temperature": 0.2}

res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data).json()
ai_text = res['choices'][0]['message']['content']
code_match = re.search(r'```dart(.*?)```', ai_text, re.DOTALL)
clean_code = code_match.group(1).strip() if code_match else ai_text.strip()

with open("project_source/lib/main.dart", "w") as f:
    f.write(clean_code)
