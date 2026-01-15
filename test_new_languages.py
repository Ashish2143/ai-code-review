#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test the new languages: TypeScript, PHP, Ruby
"""
import sys
sys.path.insert(0, 'd:\\PROJECT\\ai-code-review\\backend')

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

print("\n" + "="*80)
print("NEW LANGUAGES TEST - TypeScript, PHP, Ruby")
print("="*80)

# TypeScript
ts_code = """function greet(name: string): string {
  for (let i = 0; i < 3; i++) {
    console.log(`Hello, ${name}!`);
  }
  return `Greeted ${name}`;
}"""

response = client.post("/review", json={"code": ts_code, "language": "typescript"})
data = response.json()
print(f"\n[TYPESCRIPT]")
print(f"  Detected: {data['language']}")
print(f"  Functions: {data['features']['function_count']}")
print(f"  Loops: {data['features']['loop_count']}")
print(f"  ✓ PASS" if data['language'] == 'typescript' else "  ✗ FAIL")

# PHP
php_code = """<?php
function calculateTotal($items) {
  $total = 0;
  foreach ($items as $item) {
    $total += $item;
  }
  return $total;
}
?>"""

response = client.post("/review", json={"code": php_code, "language": "php"})
data = response.json()
print(f"\n[PHP]")
print(f"  Detected: {data['language']}")
print(f"  Functions: {data['features']['function_count']}")
print(f"  Loops: {data['features']['loop_count']}")
print(f"  ✓ PASS" if data['language'] == 'php' else "  ✗ FAIL")

# Ruby
ruby_code = """def greet_all(names)
  result = []
  names.each do |name|
    result << "Hello, \#{name}!"
  end
  result
end"""

response = client.post("/review", json={"code": ruby_code, "language": "ruby"})
data = response.json()
print(f"\n[RUBY]")
print(f"  Detected: {data['language']}")
print(f"  Functions: {data['features']['function_count']}")
print(f"  Loops: {data['features']['loop_count']}")
print(f"  ✓ PASS" if data['language'] == 'ruby' else "  ✗ FAIL")

print("\n" + "="*80)
print("✓ NEW LANGUAGES TEST COMPLETE")
print("="*80 + "\n")
