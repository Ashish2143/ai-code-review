#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Language Detection Test
Tests if different languages are properly detected and analyzed
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from multilang_analyzer import extract_features
from fastapi.testclient import TestClient
from main import app

print("=" * 80)
print("LANGUAGE DETECTION TEST")
print("=" * 80)

# Test cases for each language
test_cases = {
    "python": {
        "code": "def hello():\n    for i in range(5):\n        print(i)",
        "expected": {"function_count": 1, "loop_count": 1}
    },
    "javascript": {
        "code": "function hello() {\n    for (let i = 0; i < 5; i++) {\n        console.log(i);\n    }\n}",
        "expected": {"function_count": 1, "loop_count": 1}
    },
    "java": {
        "code": "public class Test {\n    public void run() {\n        for (int i = 0; i < 5; i++) {\n            System.out.println(i);\n        }\n    }\n}",
        "expected": {"function_count": 1, "class_count": 1, "loop_count": 1}
    },
    "cpp": {
        "code": "#include <iostream>\nint main() {\n    for (int i = 0; i < 5; i++) {\n        std::cout << i << std::endl;\n    }\n    return 0;\n}",
        "expected": {"function_count": 1, "loop_count": 1}
    },
    "csharp": {
        "code": "public class Test {\n    public void Run() {\n        for (int i = 0; i < 5; i++) {\n            Console.WriteLine(i);\n        }\n    }\n}",
        "expected": {"function_count": 1, "class_count": 1, "loop_count": 1}
    },
    "go": {
        "code": "package main\nfunc main() {\n    for i := 0; i < 5; i++ {\n        println(i)\n    }\n}",
        "expected": {"function_count": 1, "loop_count": 1}
    },
    "rust": {
        "code": "fn main() {\n    for i in 0..5 {\n        println!(\"{}\", i);\n    }\n}",
        "expected": {"function_count": 1, "loop_count": 1}
    }
}

print("\n[DIRECT ANALYZER TEST]")
print("-" * 80)

for lang, test in test_cases.items():
    try:
        result = extract_features(test["code"], lang)
        
        print(f"\n[{lang.upper()}]")
        print(f"  Functions: {result.get('function_count', 0)}")
        print(f"  Loops: {result.get('loop_count', 0)}")
        print(f"  Classes: {result.get('class_count', 0)}")
        
        # Check for errors
        if "error" in result or "syntax_error" in result:
            error_msg = result.get('error') or result.get('syntax_error')
            print(f"  [ERROR] {error_msg}")
        else:
            print(f"  [OK] Analysis successful")
            
    except Exception as e:
        print(f"\n[{lang.upper()}] [ERROR] {type(e).__name__}: {str(e)}")

print("\n" + "=" * 80)
print("[API ENDPOINT TEST]")
print("=" * 80)

client = TestClient(app)

for lang, test in test_cases.items():
    try:
        print(f"\n[{lang.upper()}]")
        response = client.post("/review", json={"code": test["code"], "language": lang})
        
        print(f"  Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"  Language Detected: {data.get('language', 'N/A')}")
            print(f"  Bug Probability: {data.get('bug_probability', 'N/A')}")
            
            features = data.get('features', {})
            print(f"  Functions: {features.get('function_count', 0)}")
            print(f"  Loops: {features.get('loop_count', 0)}")
            print(f"  Classes: {features.get('class_count', 0)}")
            
            if data.get('issues'):
                print(f"  Issues: {', '.join(data['issues'])}")
            else:
                print(f"  Issues: None")
                
            print(f"  [OK] Response successful")
        else:
            print(f"  [ERROR] Status {response.status_code}")
            print(f"  Response: {response.text}")
            
    except Exception as e:
        print(f"  [ERROR] {type(e).__name__}: {str(e)}")

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
