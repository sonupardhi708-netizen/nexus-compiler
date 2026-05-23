import os
import requests
import json
import re

# आगे-पीछे की एक्स्ट्रा स्पेस को साफ करने के लिए .strip()
raw_key = os.getenv('GROQ_API_KEY', '')
api_key = raw_key.strip().replace('"', '').replace("'", "")
prompt = os.getenv('APP_PROMPT', 'Simple dashboard app')

sys_ins = "Act as an expert Flutter Developer. Output ONLY valid, clean Dart code inside a single markdown block. No explanations."

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama3-70b-8192",
    "messages": [
        {"role": "system", "content": sys_ins},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.2
}

try:
    if not api_key:
        raise ValueError("API Key is completely empty!")
        
    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
    res_json = res.json()
    
    if 'choices' in res_json:
        ai_text = res_json['choices'][0]['message']['content']
        code_match = re.search(r'```(?:dart)?(.*?)
```', ai_text, re.DOTALL)
        clean_code = code_match.group(1).strip() if code_match else ai_text.strip()
        
        with open("project_source/lib/main.dart", "w") as f:
            f.write(clean_code)
        print("Code generated successfully!")
    else:
        print(f"API Response Error: {res_json}")
except Exception as e:
    print(f"Error occurred: {e}")
