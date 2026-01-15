#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

BASE_URL = "http://localhost:8000"

test_cases = {
    "python": {
        "code": "def calculate_sum(numbers):\n    total = 0\n    for num in numbers:\n        total += num\n    return total",
        "description": "Python function with loop"
    },
    "javascript": {
        "code": "function calculateSum(numbers) {\n  let total = 0;\n  for (let i = 0; i < numbers.length; i++) {\n    total += numbers[i];\n  }\n  return total;\n}",
        "description": "JavaScript function with loop"
    },
    "java": {
        "code": "public class Calculator {\n  public int calculateSum(int[] numbers) {\n    int total = 0;\n    for (int num : numbers) {\n      total += num;\n    }\n    return total;\n  }\n}",
        "description": "Java class with method and loop"
    },
    "cpp": {
        "code": "#include <iostream>\nusing namespace std;\nint calculateSum(int numbers[], int size) {\n  int total = 0;\n  for (int i = 0; i < size; i++) {\n    total += numbers[i];\n  }\n  return total;\n}",
        "description": "C++ function with loop"
    },
    "csharp": {
        "code": "public class Calculator {\n  public int CalculateSum(int[] numbers) {\n    int total = 0;\n    foreach (int num in numbers) {\n      total += num;\n    }\n    return total;\n  }\n}",
        "description": "C# class with foreach loop"
    },
    "go": {
        "code": "package main\nimport \"fmt\"\nfunc calculateSum(numbers []int) int {\n  total := 0\n  for _, num := range numbers {\n    total += num\n  }\n  return total\n}",
        "description": "Go function with range loop"
    },
    "rust": {
        "code": "fn calculate_sum(numbers: &[i32]) -> i32 {\n  let mut total = 0;\n  for &num in numbers {\n    total += num;\n  }\n  total\n}",
        "description": "Rust function with loop"
    }
}

print("=" * 100)
print("END-TO-END LANGUAGE DETECTION TEST")
print("=" * 100)

for language, test in test_cases.items():
    print(f"\n[{language.upper()}] - {test['description']}")
    print("-" * 100)
    
    try:
        response = requests.post(f"{BASE_URL}/review", json={
            "code": test["code"],
            "language": language
        })
        
        if response.status_code == 200:
            data = response.json()
            
            # Check the response
            detected_lang = data.get('language', 'N/A')
            bug_prob = data.get('bug_probability', 0) * 100
            features = data.get('features', {})
            
            functions = features.get('function_count', 0)
            loops = features.get('loop_count', 0)
            classes = features.get('class_count', 0)
            
            # Verification
            correct_detection = detected_lang.lower() == language.lower()
            detection_status = "✓ CORRECT" if correct_detection else "✗ WRONG"
            
            print(f"  Language Sent: {language}")
            print(f"  Language Detected: {detected_lang} {detection_status}")
            print(f"  Functions/Methods: {functions}")
            print(f"  Loops: {loops}")
            print(f"  Classes: {classes}")
            print(f"  Bug Probability: {bug_prob:.1f}%")
            
            if 'error' in data:
                print(f"  Error: {data['error']}")
            else:
                print(f"  ✓ Analysis successful")
                
        else:
            print(f"  ✗ Error: Status {response.status_code}")
            print(f"  Response: {response.text}")
            
    except Exception as e:
        print(f"  ✗ Exception: {type(e).__name__}: {str(e)}")

print("\n" + "=" * 100)
print("TEST COMPLETE")
print("=" * 100)
