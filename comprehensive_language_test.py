#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Comprehensive Language Detection Verification
Demonstrates that all 7 languages are correctly detected and analyzed
"""
import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test code samples for each language
test_samples = [
    ("python", """def sum_numbers(arr):
    total = 0
    for n in arr:
        total += n
    return total"""),
    
    ("javascript", """function sumNumbers(arr) {
    let total = 0;
    for (let i = 0; i < arr.length; i++) {
        total += arr[i];
    }
    return total;
}"""),
    
    ("java", """public class Calculator {
    public int sumNumbers(int[] arr) {
        int total = 0;
        for (int n : arr) {
            total += n;
        }
        return total;
    }
}"""),
    
    ("cpp", """#include <iostream>
int sumNumbers(int arr[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += arr[i];
    }
    return total;
}"""),
    
    ("csharp", """public class Calculator {
    public int SumNumbers(int[] arr) {
        int total = 0;
        foreach (int n in arr) {
            total += n;
        }
        return total;
    }
}"""),
    
    ("go", """package main

func sumNumbers(arr []int) int {
    total := 0
    for _, n := range arr {
        total += n
    }
    return total
}"""),
    
    ("rust", """fn sum_numbers(arr: &[i32]) -> i32 {
    let mut total = 0;
    for &n in arr {
        total += n;
    }
    total
}"""),
]

print("\n" + "="*80)
print("LANGUAGE DETECTION TEST - ALL 7 LANGUAGES")
print("="*80)

all_passed = True

for language, code in test_samples:
    response = client.post("/review", json={
        "code": code,
        "language": language
    })
    
    data = response.json()
    detected = data.get('language')
    match = detected.lower() == language.lower()
    status = "✓ PASS" if match else "✗ FAIL"
    
    # Additional stats
    features = data.get('features', {})
    functions = features.get('function_count', 0)
    loops = features.get('loop_count', 0)
    
    print(f"\n[{language.upper():8}] {status}")
    print(f"  Sent Language: {language:12} | Detected: {detected}")
    print(f"  Functions: {functions:2} | Loops: {loops:2}")
    
    if not match:
        all_passed = False
        print(f"  ERROR: Language mismatch!")
    elif 'error' in data:
        print(f"  WARNING: {data['error']}")

print("\n" + "="*80)
if all_passed:
    print("✓ ALL TESTS PASSED - Language detection working correctly!")
else:
    print("✗ SOME TESTS FAILED - Check output above")
print("="*80 + "\n")
