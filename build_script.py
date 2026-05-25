import os
import sys

def generate_layout():
    print(">> 🤖 Nexus UI Engine Starting...")
    
    # स्केचवेयर से आ रहे वेरिएबल्स को रीड करना
    prompt = os.getenv("APP_PROMPT", "Premium App").strip()
    app_name = os.getenv("APP_NAME", "NexusApp").strip()
    
    print(f">> Processing layout for Prompt: '{prompt}'")
    print(f">> Target App Name: {app_name}")

    # 🎨 कस्टमाइज़्ड प्रीमियम लेआउट आर्किटेक्चर (Dynamic Code Injection)
    # यहाँ डार्ट का पूरा कोड ट्रिपल कोट्स के अंदर पूरी तरह सुरक्षित है!
    dart_code = f"""import 'package:flutter/material.dart';

void main() => runApp(NexusGeneratedApp());

class NexusGeneratedApp extends StatelessWidget {{
  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: '{app_name}',
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF06060C),
        primaryColor: const Color(0xFF00FFCC),
      ),
      home: MainProductionWorkspace(),
    );
  }}
}}

class MainProductionWorkspace extends StatelessWidget {{
  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      body: SafeArea(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // 🛑 COMPONENT 1: PREMIUM HEADER
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 20),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        '{app_name.upper()} AI LIVE',
                        style: TextStyle(
                          fontSize: 22,
                          color: const Color(0xFF00FFCC),
                          fontWeight: FontWeight.bold,
                          letterSpacing: 2,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        'Engine Status: Synchronized',
                        style: TextStyle(fontSize: 12, color: Colors.grey[500]),
                      ),
                    ],
                  ),
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: const Color(0xFF121225),
                      borderRadius: BorderRadius.circular(50),
                      border: Border.all(color: const Color(0xFF00FFCC).withOpacity(0.3)),
                    ),
                    child: const Icon(Icons.bolt, color: Color(0xFF00FFCC), size: 20),
                  ),
                ],
              ),
            ),

            // 🛑 COMPONENT 2: DYNAMIC USER PROMPT DISPLAY CARD
            Container(
              margin: const EdgeInsets.symmetric(horizontal: 20),
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: const Color(0xFF0F0F20),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: const Color(0xFF3F51B5).withOpacity(0.4)),
              ),
              child: Row(
                children: [
                  const Icon(Icons.psychology, color: Colors.amber, size: 30),
                  const SizedBox(width: 15),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          'COMPILED ARCHITECTURE FOR:',
                          style: TextStyle(fontSize: 10, color: Colors.amber, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          '{prompt}',
                          style: const TextStyle(fontSize: 13, color: Colors.white, height: 1.3),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 20),

            // 🛑 COMPONENT 3: LIVE RENDERED VIEWPORT / CONTENT GRID
            Expanded(
              child: Container(
                margin: const EdgeInsets.symmetric(horizontal: 20),
                decoration: BoxDecoration(
                  color: const Color(0xFF030307),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: const Color(0xFF222244)),
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(16),
                  child: ListView(
                    physics: const BouncingScrollPhysics(),
                    padding: const EdgeInsets.all(16),
                    children: [
                      _buildCryptoCard('Core Engine Pipeline', 'ACTIVE', const Color(0xFF00FFCC)),
                      _buildCryptoCard('Secure Network Bridge', 'SECURE', const Color(0xFF3F51B5)),
                      _buildCryptoCard('JSON UI Interpreter', 'STABLE', Colors.amber),
                      const SizedBox(height: 20),
                      Center(
                        child: Text(
                          '<< SYSTEM PIPELINE FULLY FUNCTIONAL >>',
                          style: TextStyle(fontSize: 11, color: Colors.grey[700], fontFamily: 'monospace'),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),

            // 🛑 COMPONENT 4: SMOOTH BOTTOM NAVIGATION BAR
            BottomNavigationBar(
              backgroundColor: const Color(0xFF0A0A16),
              selectedItemColor: const Color(0xFF00FFCC),
              unselectedItemColor: Colors.grey[600],
              currentIndex: 0,
              type: BottomNavigationBarType.fixed,
              elevation: 0,
              items: const [
                BottomNavigationBarItem(icon: Icon(Icons.grid_view_rounded), label: 'Terminal'),
                BottomNavigationBarItem(icon: Icon(Icons.layers_rounded), label: 'Modules'),
                BottomNavigationBarItem(icon: Icon(Icons.settings_suggest_rounded), label: 'Config'),
              ],
            ),
          ],
        ),
      ),
    );
  }}

  Widget _buildCryptoCard(String title, String status, Color accentColor) {{
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF121225),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: const TextStyle(fontSize: 14, color: Colors.white, fontWeight: FontWeight.w500),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: accentColor.withOpacity(0.1),
              borderRadius: BorderRadius.circular(6),
              border: Border.all(color: accentColor.withOpacity(0.5)),
            ),
            child: Text(
              status,
              style: TextStyle(fontSize: 10, color: accentColor, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );
  }}
}}
"""

    try:
        # सुनिश्चित करना कि 'lib' डायरेक्टरी मौजूद है
        os.makedirs('lib', exist_ok=True)
        
        # main.dart फ़ाइल लिखना
        target_file = 'lib/main.dart'
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(dart_code)
            
        print(">> 🟢 SUCCESS: Fresh Dart code mapped and saved to lib/main.dart!")
        
    except Exception as e:
        print(f">> ❌ Build Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    generate_layout()
  
