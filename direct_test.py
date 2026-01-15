"""
Simple test to check error handling
"""

# Test the analyzer directly
from backend.analyzer import extract_features

print("=" * 80)
print("Testing Code Analyzer with Multiple Languages/Scenarios")
print("=" * 80)

test_cases = {
    "Python - Valid Code": """
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
""",
    
    "Python - Long Function": """
def long_function():
    x = 1
    y = 2
    z = 3
    a = 4
    b = 5
    c = 6
    d = 7
    e = 8
    f = 9
    g = 10
    h = 11
    i = 12
    j = 13
    k = 14
    l = 15
    m = 16
    n = 17
    o = 18
    p = 19
    q = 20
    r = 21
    s = 22
    t = 23
    u = 24
    v = 25
    return u
""",
    
    "Python - Many Loops": """
def nested_loops():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            pass
""",
    
    "JavaScript (Not Python)": """
function calculateSum(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}
""",
    
    "Python - Invalid Syntax": """
def invalid_func(
    x = 1
    y = 2
    return x + y
""",
    
    "Empty Code": "",
}

for test_name, code in test_cases.items():
    print(f"\n[TEST] {test_name}")
    print("-" * 80)
    
    try:
        features = extract_features(code)
        
        if "syntax_error" in features:
            print(f"✗ SYNTAX ERROR detected")
            print(f"  Error: {features['syntax_error']}")
        elif "parse_error" in features:
            print(f"✗ PARSE ERROR detected")
            print(f"  Error: {features['parse_error']}")
        else:
            print(f"✓ Analysis successful")
            print(f"  avg_func_len: {features.get('avg_func_len', 0):.2f}")
            print(f"  loop_count: {features.get('loop_count', 0)}")
            
    except Exception as e:
        print(f"✗ EXCEPTION: {type(e).__name__}")
        print(f"  Error: {str(e)}")

print("\n" + "=" * 80)
print("Testing Complete")
print("=" * 80)
