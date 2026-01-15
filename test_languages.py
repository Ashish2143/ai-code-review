import requests
import json

BASE_URL = "http://localhost:8000"

# Test cases with different languages
test_cases = {
    "Python - Valid Code": {
        "code": """
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = calculate_sum([1, 2, 3, 4, 5])
print(result)
""",
        "language": "python"
    },
    
    "Python - Long Function": {
        "code": """
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
    w = 26
    x = 27
    y = 28
    z = 29
    return x + y + z
""",
        "language": "python"
    },
    
    "Python - Many Loops": {
        "code": """
def nested_loops():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            print(i, j, k, l, m, n)
""",
        "language": "python"
    },
    
    "JavaScript Code": {
        "code": """
function calculateSum(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total;
}
""",
        "language": "javascript"
    },
    
    "Java Code": {
        "code": """
public class Calculator {
    public static int sum(int[] numbers) {
        int total = 0;
        for (int num : numbers) {
            total += num;
        }
        return total;
    }
}
""",
        "language": "java"
    },
    
    "C++ Code": {
        "code": """
#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }
    cout << sum << endl;
    return 0;
}
""",
        "language": "cpp"
    },
    
    "Python - Invalid Syntax": {
        "code": """
def invalid_func(
    x = 1
    y = 2
    return x + y
""",
        "language": "python"
    },
    
    "Empty Code": {
        "code": "",
        "language": "python"
    },
}

print("=" * 80)
print("Testing AI Code Review with Multiple Languages")
print("=" * 80)

for test_name, test_data in test_cases.items():
    print(f"\n[TEST] {test_name}")
    print("-" * 80)
    
    try:
        response = requests.post(
            f"{BASE_URL}/review",
            json={"code": test_data["code"]},
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✓ Status: SUCCESS")
            print(f"  Bug Probability: {result.get('bug_probability', 'N/A')}")
            print(f"  Issues: {result.get('issues', [])}")
            print(f"  Suggestions: {result.get('suggestions', [])}")
        else:
            print(f"✗ Status: ERROR {response.status_code}")
            print(f"  Response: {response.text}")
    except Exception as e:
        print(f"✗ Exception: {type(e).__name__}")
        print(f"  Error: {str(e)}")

print("\n" + "=" * 80)
print("Testing Complete")
print("=" * 80)
