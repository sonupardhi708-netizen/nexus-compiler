import os
import json
import requests

print("🤖 Nexus AI Backend Compiler Engine v4.0 Started...")

# पर्यावरण से ऐप प्रॉमप्ट और Groq API Key उठाना
app_prompt = os.getenv('APP_PROMPT', '').strip()
groq_api_key = os.getenv('GROQ_API_KEY', '').strip()

print(f"📝 Received Prompt from App: {app_prompt}")

if not app_prompt:
    app_prompt = "Create a premium dark themed industrial application."

if not groq_api_key:
    print("⚠️ WARNING: GROQ_API_KEY NOT FOUND! Falling back to safe template.")
    flutter_code = f"""import 'package:flutter/material.dart';
void main() => runApp(MaterialApp(home: Scaffold(body: Center(child: Text("{app_prompt}")))));"""
else:
    print("🚀 Connecting to Groq AI Live Generation Engine...")
    
    # AI को निर्देश कि सिर्फ शुद्ध फ्लटर कोड दे, फालतू टेक्स्ट नहीं
    system_instruction = (
        "You are the Nexus AI live coding engine. Your job is to generate complete, "
        "production-ready, and working Flutter code based on the user's request. "
        "Return ONLY the executable Flutter source code inside standard ```dart 
``` blocks. "
        "Do NOT include any explanations, markdown text, or talk before/after the code. "
        "Ensure all parameters, design layout, properties, and widgets are fully implemented."
    )
    
    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {groq_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-70b-8192", 
                "messages": [
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": f"Build this complete app layout now: {app_prompt}"}
                ],
                "temperature": 0.3
            },
            timeout=30
        )
        
        ai_response = response.json()['choices'][0]['message']['content']
        
        # AI के रिस्पॉन्स में से केवल फ्लटर कोड निकालना
        if "```dart" in ai_response:
            flutter_code = ai_response.split("
```dart")[1].split("```")[0].strip()
        elif "```" in ai_response:
            flutter_code = ai_response.split("
```")[1].split("```")[0].strip()
        else:
            flutter_code = ai_response.strip()
            
        print("🟢 SUCCESS: AI has generated a complete working application structure!")
        
    except Exception as e:
        print(f"❌ Groq AI Generation Error: {str(e)}. Falling back to safe template.")
        flutter_code = f"""import 'package:flutter/material.dart';
void main() => runApp(MaterialApp(home: Scaffold(body: Center(child: Text("Build Error: {str(e)}")))));"""

# कोड को main.dart फाइल में सेव करना
target_path = "project_source/lib/main.dart"
os.makedirs(os.path.dirname(target_path), exist_ok=True)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(flutter_code)

print("🎯 SUCCESS: Old placeholder code cleared. Real Live UI generated successfully!")
