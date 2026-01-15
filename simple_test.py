#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from multilang_analyzer import extract_features

# Test Python code
python_code = "def hello():\n    for i in range(5):\n        print(i)"
python_result = extract_features(python_code, "python")
print(f"Python: {python_result}")

# Test JavaScript code  
js_code = "function hello() { for (let i = 0; i < 5; i++) { console.log(i); } }"
js_result = extract_features(js_code, "javascript")
print(f"JavaScript: {js_result}")

# Test Java code
java_code = "public class Test { public void run() { for (int i = 0; i < 5; i++) { System.out.println(i); } } }"
java_result = extract_features(java_code, "java")
print(f"Java: {java_result}")

# Test with wrong language passed
wrong_result = extract_features(js_code, "python")
print(f"JavaScript code with python language: {wrong_result}")
