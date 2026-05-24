import os
import json

print("🤖 Nexus AI Backend Compiler Engine v3.0 Started...")

# ऐप प्रॉम्प्ट को एनवायरनमेंट से उठाना
app_prompt = os.getenv('APP_PROMPT', '').strip()

print(f"📝 Received Prompt from Sketchware: {app_prompt}")

if not app_prompt:
    app_prompt = "Create a premium dark themed industrial application."

clean_text = app_prompt.replace('"', '\\"').replace('\n', ' ')

# फ्लटर का पूरा बेस कोड बिना f-string के (ताकि ब्रैकेट्स क्रैश न हों)
flutter_template = """import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xff06060c),
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
                  const Icon(Icons.auto_awesome, color: Color(0xff00ffcc), size: 60),
                  const SizedBox(height: 25),
                  const Text(
                    'NEXUS GENERATED LIVE UI',
                    style: TextStyle(
                      color: Color(0xff00ffcc),
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 2,
                    ),
                  ),
                  const SizedBox(height: 20),
                  Card(
                    color: const Color(0xff111122),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                      side: const BorderSide(color: Color(0xff222244), width: 1),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(20.0),
                      child: Text(
                        "PLACEHOLDER_TEXT",
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
  }
}"""

# यहाँ पर प्रॉमप्ट को सुरक्षित तरीके से फ्लटर कोड में इंजेक्ट करना
flutter_code = flutter_template.replace("PLACEHOLDER_TEXT", clean_text)

target_path = "project_source/lib/main.dart"
os.makedirs(os.path.dirname(target_path), exist_ok=True)

with open(target_path, "w", encoding="utf-8") as f:
    f.write(flutter_code)

print("🎯 SUCCESS: Old build code cleared. New clean Flutter UI generated successfully!")
