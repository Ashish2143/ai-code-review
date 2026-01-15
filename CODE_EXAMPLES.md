# Code Examples for AI Code Review

## 1. Python Example
```python
def fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 1:
        return n
    
    for i in range(n):
        a, b = 0, 1
        while a < n:
            print(a)
            a, b = b, a + b
    
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)
print(result)
```

**Expected Analysis:**
- Functions: 1
- Loops: 2
- Classes: 0
- Avg Function Length: ~13 lines
- Issues: Maybe "Many loops"

---

## 2. JavaScript Example
```javascript
class UserManager {
    constructor(users = []) {
        this.users = users;
    }
    
    addUser(user) {
        this.users.push(user);
        return this.users.length;
    }
    
    findUser(id) {
        for (let i = 0; i < this.users.length; i++) {
            if (this.users[i].id === id) {
                return this.users[i];
            }
        }
        return null;
    }
    
    displayAll() {
        this.users.forEach(user => {
            console.log(user.name);
        });
    }
}

const manager = new UserManager();
manager.addUser({id: 1, name: "John"});
```

**Expected Analysis:**
- Functions: 4
- Loops: 2 (for + forEach)
- Classes: 1
- Avg Function Length: ~5 lines

---

## 3. Java Example
```java
public class DataProcessor {
    private List<Integer> data;
    
    public DataProcessor(List<Integer> input) {
        this.data = input;
    }
    
    public int calculateSum() {
        int sum = 0;
        for (int num : this.data) {
            sum += num;
        }
        return sum;
    }
    
    public void processData() {
        for (Integer value : this.data) {
            for (Integer other : this.data) {
                if (value > other) {
                    System.out.println(value);
                }
            }
        }
    }
    
    public List<Integer> filter(int threshold) {
        List<Integer> result = new ArrayList<>();
        for (Integer num : this.data) {
            if (num > threshold) {
                result.add(num);
            }
        }
        return result;
    }
}
```

**Expected Analysis:**
- Functions: 4 methods
- Loops: 4 (nested and sequential)
- Classes: 1
- Issues: "Many loops", "Long functions"

---

## 4. C++ Example
```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {5, 2, 8, 1, 9};
    
    // Bubble sort
    for (int i = 0; i < numbers.size(); i++) {
        for (int j = 0; j < numbers.size() - 1; j++) {
            if (numbers[j] > numbers[j + 1]) {
                int temp = numbers[j];
                numbers[j] = numbers[j + 1];
                numbers[j + 1] = temp;
            }
        }
    }
    
    // Print sorted array
    for (int num : numbers) {
        std::cout << num << " ";
    }
    
    return 0;
}
```

**Expected Analysis:**
- Functions: 1
- Loops: 3 (nested bubble sort + final loop)
- Classes: 0
- Avg Function Length: ~17 lines

---

## 5. C# Example
```csharp
public class ShoppingCart {
    private List<Item> items;
    
    public ShoppingCart() {
        items = new List<Item>();
    }
    
    public void AddItem(Item item) {
        items.Add(item);
    }
    
    public decimal CalculateTotal() {
        decimal total = 0;
        foreach (var item in items) {
            total += item.Price * item.Quantity;
        }
        return total;
    }
    
    public void ApplyDiscount(decimal percentage) {
        decimal discount = CalculateTotal() * (percentage / 100);
        foreach (var item in items) {
            item.Price -= (item.Price * (percentage / 100));
        }
    }
}
```

**Expected Analysis:**
- Functions: 4 methods
- Loops: 2 (foreach loops)
- Classes: 1
- Avg Function Length: ~4 lines

---

## 6. Go Example
```go
package main

import "fmt"

func main() {
    numbers := []int{3, 1, 4, 1, 5, 9}
    
    // Print all numbers
    for i, num := range numbers {
        fmt.Printf("%d: %d\n", i, num)
    }
    
    // Count occurrences
    counts := make(map[int]int)
    for _, num := range numbers {
        counts[num]++
    }
    
    // Print counts
    for num, count := range counts {
        fmt.Printf("%d appears %d times\n", num, count)
    }
}
```

**Expected Analysis:**
- Functions: 1
- Loops: 3 (range loops)
- Classes: 0
- Avg Function Length: ~17 lines

---

## 7. Rust Example
```rust
fn main() {
    let numbers = vec![1, 2, 3, 4, 5];
    
    // First loop
    for num in &numbers {
        println!("{}", num);
    }
    
    // While loop
    let mut i = 0;
    while i < 5 {
        println!("Count: {}", i);
        i += 1;
    }
    
    // Infinite loop with break
    loop {
        if i > 10 {
            break;
        }
        println!("Loop: {}", i);
        i += 1;
    }
}
```

**Expected Analysis:**
- Functions: 1
- Loops: 3 (for + while + loop)
- Classes: 0
- Avg Function Length: ~19 lines

---

## Copy & Paste Test

1. Copy any of these examples
2. Go to http://localhost:8000
3. Select the corresponding language
4. Paste the code
5. Click "Analyze Code"
6. See the results!

