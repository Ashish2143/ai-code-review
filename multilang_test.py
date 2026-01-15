"""
Complete multi-language test suite for AI Code Review
Tests all supported programming languages
"""

import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from multilang_analyzer import extract_features

# Test cases for all supported languages
test_cases = {
    "Python - Simple": {
        "language": "python",
        "code": """
def greet(name):
    message = f"Hello, {name}!"
    return message

for i in range(5):
    print(greet(f"User{i}"))
"""
    },
    
    "JavaScript - Event Handler": {
        "language": "javascript",
        "code": """
function handleClick(event) {
    const element = event.target;
    element.classList.add('active');
    
    for (let i = 0; i < 10; i++) {
        console.log(i);
    }
}

document.addEventListener('click', handleClick);
"""
    },
    
    "Java - Class Example": {
        "language": "java",
        "code": """
public class Calculator {
    private int value;
    
    public Calculator(int initial) {
        this.value = initial;
    }
    
    public int add(int num) {
        this.value += num;
        return this.value;
    }
    
    public void printLoop() {
        for (int i = 0; i < 10; i++) {
            System.out.println(i);
        }
    }
}
"""
    },
    
    "C++ - Function": {
        "language": "cpp",
        "code": """
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << numbers[i] << std::endl;
    }
    
    return 0;
}
"""
    },
    
    "C# - Method": {
        "language": "csharp",
        "code": """
public class Person {
    public string Name { get; set; }
    
    public void PrintNames(string[] names) {
        foreach (var name in names) {
            Console.WriteLine(name);
        }
    }
    
    public int CalculateSum(int[] numbers) {
        int sum = 0;
        foreach (int num in numbers) {
            sum += num;
        }
        return sum;
    }
}
"""
    },
    
    "Go - Function": {
        "language": "go",
        "code": """
package main

import "fmt"

func main() {
    numbers := []int{1, 2, 3, 4, 5}
    
    for i, num := range numbers {
        fmt.Println(i, num)
    }
    
    for i := 0; i < 10; i++ {
        fmt.Println(i)
    }
}
"""
    },
    
    "Rust - Function": {
        "language": "rust",
        "code": """
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    
    for num in &numbers {
        println!("{}", num);
    }
    
    loop {
        println!("Hello");
        break;
    }
    
    while true {
        println!("Loop");
        break;
    }
}
"""
    },
    
    "Python - Invalid Syntax": {
        "language": "python",
        "code": """
def broken_function(
    x = 1
    y = 2
    return x + y
"""
    },
    
    "JavaScript - Syntax Error": {
        "language": "javascript",
        "code": """
function broken() {
    console.log("hello"
    return x;
}
"""
    },
}

print("=" * 100)
print("AI CODE REVIEW - MULTI-LANGUAGE TEST SUITE")
print("=" * 100)

for test_name, test_data in test_cases.items():
    print(f"\n{'='*100}")
    print(f"[TEST] {test_name}")
    print(f"{'='*100}")
    
    language = test_data["language"]
    code = test_data["code"]
    
    try:
        features = extract_features(code, language)
        
        # Check for errors
        if "syntax_error" in features:
            print(f"❌ SYNTAX ERROR")
            print(f"   Error: {features['syntax_error']}")
        elif "parse_error" in features:
            print(f"❌ PARSE ERROR")
            print(f"   Error: {features['parse_error']}")
        elif "error" in features:
            print(f"❌ ERROR")
            print(f"   Error: {features['error']}")
        else:
            print(f"✅ ANALYSIS SUCCESSFUL")
            print(f"\n   📊 Metrics:")
            print(f"      • Functions/Methods: {features.get('function_count', 0)}")
            print(f"      • Loops: {features.get('loop_count', 0)}")
            print(f"      • Classes: {features.get('class_count', 0)}")
            print(f"      • Avg Function Length: {features.get('avg_func_len', 0):.2f} lines")
            
    except Exception as e:
        print(f"❌ EXCEPTION: {type(e).__name__}")
        print(f"   {str(e)}")

print(f"\n{'='*100}")
print("TEST SUITE COMPLETE")
print("=" * 100)
