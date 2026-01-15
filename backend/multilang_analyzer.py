import ast
from typing import Dict, Any

def extract_features_python(code: str) -> Dict[str, Any]:
    """Python-specific feature extractor using AST."""
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "function_count": 0,
            "class_count": 0,
            "syntax_error": str(e),
        }
    except Exception as e:
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "function_count": 0,
            "class_count": 0,
            "parse_error": str(e),
        }

    class Visitor(ast.NodeVisitor):
        def __init__(self):
            self.loop_count = 0
            self.func_lens = []
            self.class_count = 0
            self.function_count = 0

        def visit_FunctionDef(self, node):
            self.function_count += 1
            start = node.lineno
            end = getattr(node, 'end_lineno', node.lineno)
            self.func_lens.append(end - start + 1)
            self.generic_visit(node)

        def visit_AsyncFunctionDef(self, node):
            self.function_count += 1
            start = node.lineno
            end = getattr(node, 'end_lineno', node.lineno)
            self.func_lens.append(end - start + 1)
            self.generic_visit(node)

        def visit_ClassDef(self, node):
            self.class_count += 1
            self.generic_visit(node)

        def visit_For(self, node):
            self.loop_count += 1
            self.generic_visit(node)

        def visit_While(self, node):
            self.loop_count += 1
            self.generic_visit(node)

    v = Visitor()
    v.visit(tree)

    avg_func_len = sum(v.func_lens) / len(v.func_lens) if v.func_lens else 0
    return {
        "avg_func_len": avg_func_len,
        "loop_count": v.loop_count,
        "function_count": v.function_count,
        "class_count": v.class_count,
    }


def extract_features_javascript(code: str) -> Dict[str, Any]:
    """JavaScript feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('function ') + code.count('() =>'),
        "loop_count": code.count('for ') + code.count('while ') + code.count('.forEach('),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    # Calculate average function length
    import re
    functions = re.findall(r'(?:function|=>).*?\{', code)
    if functions:
        lines = code.split('\n')
        features["avg_func_len"] = len(lines) / len(functions) if functions else 0
    
    return features


def extract_features_java(code: str) -> Dict[str, Any]:
    """Java feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('public ') + code.count('private ') + code.count('protected '),
        "loop_count": code.count('for ') + code.count('while ') + code.count('do {'),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_cpp(code: str) -> Dict[str, Any]:
    """C++ feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('void ') + code.count('int ') + code.count('double ') + code.count('bool '),
        "loop_count": code.count('for ') + code.count('while ') + code.count('do {'),
        "class_count": code.count('class ') + code.count('struct '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_csharp(code: str) -> Dict[str, Any]:
    """C# feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('public ') + code.count('private ') + code.count('protected '),
        "loop_count": code.count('for ') + code.count('while ') + code.count('foreach '),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_go(code: str) -> Dict[str, Any]:
    """Go feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('func '),
        "loop_count": code.count('for ') + code.count('range '),
        "class_count": code.count('type '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_rust(code: str) -> Dict[str, Any]:
    """Rust feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('fn '),
        "loop_count": code.count('for ') + code.count('while ') + code.count('loop {'),
        "class_count": code.count('struct ') + code.count('impl '),
        "avg_func_len": 0,
    }
    
    # Basic syntax check
    if code.count('{') != code.count('}'):
        features["syntax_error"] = "Mismatched braces: { count != } count"
    if code.count('(') != code.count(')'):
        features["syntax_error"] = "Mismatched parentheses: ( count != ) count"
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_typescript(code: str) -> Dict[str, Any]:
    """TypeScript feature extractor - similar to JavaScript."""
    features = {
        "function_count": code.count('function ') + code.count('() =>') + code.count('() :'),
        "loop_count": code.count('for ') + code.count('while ') + code.count('.forEach('),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_php(code: str) -> Dict[str, Any]:
    """PHP feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('function '),
        "loop_count": code.count('for ') + code.count('foreach ') + code.count('while '),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features_ruby(code: str) -> Dict[str, Any]:
    """Ruby feature extractor - basic pattern matching."""
    features = {
        "function_count": code.count('def '),
        "loop_count": code.count('while ') + code.count('for ') + code.count('.each'),
        "class_count": code.count('class '),
        "avg_func_len": 0,
    }
    
    lines = code.split('\n')
    features["avg_func_len"] = len(lines) / max(features["function_count"], 1)
    
    return features


def extract_features(code: str, language: str = "python") -> Dict[str, Any]:
    """Extract features based on programming language."""
    language = language.lower().strip()
    
    if not code or not code.strip():
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "function_count": 0,
            "class_count": 0,
            "language": language,
        }
    
    if language == "python":
        return {**extract_features_python(code), "language": language}
    elif language in ["javascript", "js"]:
        return {**extract_features_javascript(code), "language": language}
    elif language in ["typescript", "ts"]:
        return {**extract_features_typescript(code), "language": language}
    elif language == "java":
        return {**extract_features_java(code), "language": language}
    elif language in ["cpp", "c++"]:
        return {**extract_features_cpp(code), "language": language}
    elif language in ["csharp", "c#"]:
        return {**extract_features_csharp(code), "language": language}
    elif language == "go":
        return {**extract_features_go(code), "language": language}
    elif language == "rust":
        return {**extract_features_rust(code), "language": language}
    elif language == "php":
        return {**extract_features_php(code), "language": language}
    elif language == "ruby":
        return {**extract_features_ruby(code), "language": language}
    else:
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "function_count": 0,
            "class_count": 0,
            "language": language,
            "error": f"Unsupported language: {language}",
        }
