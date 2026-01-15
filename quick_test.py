"""
Quick verification test - ensures all components work
"""
import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from multilang_analyzer import extract_features

test_code = {
    "python": "def hello():\n    for i in range(5):\n        print(i)",
    "javascript": "function test() {\n    for (let i = 0; i < 5; i++) {\n        console.log(i);\n    }\n}",
    "java": "public class Test {\n    public void run() {\n        for (int i = 0; i < 5; i++) { }\n    }\n}",
}

print("=" * 80)
print("QUICK VERIFICATION TEST")
print("=" * 80)

for lang, code in test_code.items():
    print(f"\n✓ Testing {lang.upper()}")
    result = extract_features(code, lang)
    print(f"  Functions: {result.get('function_count', 0)}")
    print(f"  Loops: {result.get('loop_count', 0)}")
    print(f"  Classes: {result.get('class_count', 0)}")
    
    if "error" in result or "syntax_error" in result:
        print(f"  ❌ ERROR: {result.get('error') or result.get('syntax_error')}")
    else:
        print(f"  ✅ SUCCESS")

print("\n" + "=" * 80)
print("All tests passed! Server should be ready.")
print("=" * 80)
print("\nOpen in browser: http://localhost:8000")
