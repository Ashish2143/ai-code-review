#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import io

# Fix encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 80)
print("ERROR DETECTION TEST")
print("=" * 80)

# Test 1: Import main
try:
    sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')
    print("\n[TEST 1] Importing main.py...")
    from main import app
    print("[OK] SUCCESS: main imported")
except Exception as e:
    print(f"[ERROR] ERROR in main.py: {type(e).__name__}")
    print(f"   Message: {str(e)}")
    import traceback
    traceback.print_exc()

# Test 2: Import analyzer
try:
    print("\n[TEST 2] Importing multilang_analyzer.py...")
    from multilang_analyzer import extract_features
    print("[OK] SUCCESS: multilang_analyzer imported")
except Exception as e:
    print(f"[ERROR] ERROR in multilang_analyzer: {type(e).__name__}")
    print(f"   Message: {str(e)}")

# Test 3: Test extract_features
try:
    print("\n[TEST 3] Testing extract_features function...")
    result = extract_features("def test(): pass", "python")
    print(f"[OK] SUCCESS: Feature extraction works")
    print(f"   Result: {result}")
except Exception as e:
    print(f"[ERROR] ERROR in extract_features: {type(e).__name__}")
    print(f"   Message: {str(e)}")

# Test 4: Check API response
try:
    print("\n[TEST 4] Testing FastAPI app...")
    from fastapi.testclient import TestClient
    client = TestClient(app)
    response = client.post("/review", json={"code": "def test(): pass", "language": "python"})
    print(f"[OK] API Response Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"   Bug Probability: {data.get('bug_probability', 'N/A')}")
        print(f"   Language: {data.get('language', 'N/A')}")
        print(f"   Issues: {data.get('issues', [])}")
    else:
        print(f"[ERROR] ERROR: {response.text}")
except Exception as e:
    print(f"[ERROR] ERROR testing API: {type(e).__name__}")
    print(f"   Message: {str(e)}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
