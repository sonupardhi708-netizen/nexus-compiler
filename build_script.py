import os, requests
prompt = os.getenv('APP_PROMPT', 'Industrial App')
# .strip() लगा दिया ताकि फालतू स्पेस या न्यू-लाइन अपने आप हट जाए
key = os.getenv('GROQ_API_KEY', '').strip().replace('*', '')
url = "https://api.groq.com/openai/v1/chat/completions"
head = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
body = {"model": "llama3-70b-8192", "messages": [{"role": "user", "content": f"Give only pure executable Flutter code for: {prompt}"}], "temperature": 0.2}

try:
    res = requests.post(url, headers=head, json=body).json()
    code = res['choices'][0]['message']['content'].replace('```dart', '').replace('```', '')
except Exception as e:
    # अगर चाबी फिर भी गड़बड़ रही, तो ऐप क्रैश नहीं होगा, एरर स्क्रीन बना देगा
    code = f"import 'package:flutter/material.dart';\nvoid main() => runApp(MaterialApp(home: Scaffold(body: Center(child: Text('API Key Error: {str(e)}')))));"

os.makedirs('project_source/lib', exist_ok=True)
with open('project_source/lib/main.dart', 'w') as f: f.write(code)
print("SUCCESS")
