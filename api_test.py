#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test with JavaScript code
js_code = "function hello() { for (let i = 0; i < 5; i++) { console.log(i); } }"

print("=" * 80)
print("API TEST: JavaScript code with 'javascript' language")
print("=" * 80)

response = client.post("/review", json={
    "code": js_code,
    "language": "javascript"
})

print(f"\nStatus Code: {response.status_code}")
data = response.json()

print(f"Language Detected: {data.get('language')}")
print(f"Functions Found: {data['features'].get('function_count')}")
print(f"Loops Found: {data['features'].get('loop_count')}")
print(f"Response Keys: {list(data.keys())}")
print(f"Full Features: {data.get('features')}")

print("\n" + "=" * 80)
print("API TEST: JavaScript code with 'python' language (WRONG)")
print("=" * 80)

response2 = client.post("/review", json={
    "code": js_code,
    "language": "python"
})

print(f"\nStatus Code: {response2.status_code}")
data2 = response2.json()

print(f"Language Detected: {data2.get('language')}")
print(f"Has Error: {'error' in data2}")
if 'error' in data2:
    print(f"Error: {data2['error']}")
print(f"Full Response: {data2}")
