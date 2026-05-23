import os
import json

print("🤖 Nexus AI Backend Compiler Engine v3.0 Started...")

# 📥 गिटहब एनवायरनमेंट से ऐप का पेलोड उठाना
app_prompt = os.getenv("APP_PROMPT", "").strip()

print(f"📥 Received Prompt from Sketchware: {app_prompt}")

# अगर प्रॉमप्ट खाली है या उसमें कोई कोड नहीं है तो एक क्लीन डिफ़ॉल्ट टेम्पलेट सेट करना
if not app_prompt:
    app_prompt = "Create a premium dark themed industrial application."

# 🛡️ सेफ़ कोडिंग: कोट्स को एस्केप करना ताकि पाइथन का सिंटैक्स कभी न टूटे
clean_text = app_prompt.replace('"', '\\"').replace('\n', ' ')

# 🏗️ पूरा फ़्लटर आर्किटेक्चर स्ट्रक्चर (Triple Quotes के साथ)
flutter_code = f"""import 'package:flutter/material.dart';

void main() {{
  runApp(const MyApp());
}}

class MyApp extends StatelessWidget {{
  const MyApp({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF06060C),
      ),
      home: Scaffold(
        body: SafeArea(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  const Icon(Icons.auto_awesome, color: Color(0xFF00FFCC), size: 60),
                  const SizedBox(height: 25),
                  const Text(
                    'NEXUS GENERATED LIVE UI',
                    style: TextStyle(
                      color: Color(0xFF00FFCC),
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 2,
                    ),
                  ),
                  const SizedBox(height: 20),
                  Card(
                    color: const Color(0xFF111122),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                      side: const BorderSide(color: Color(0xFF222244), width: 1),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(20.0),
                      child: Text(
                        "{clean_text}",
                        style: const TextStyle(
                          color: Colors.white, 
                          fontSize: 14, 
                          height: 1.5,
                          fontFamily: 'monospace',
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }}
}}
"""

# 💾 फ़्लटर के main.dart में कोड को सुरक्षित ओवरराइट करना (🚨 ये लाइनें बहुत ज़रूरी हैं भाई!)
target_path = "project_source/lib/main.dart"
os.makedirs(os.path.dirname(target_path), exist_ok=True)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(flutter_code)

print("🎯 SUCCESS: Old build code cleared. New clean Flutter UI generated successfully!")
