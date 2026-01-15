import ast

def extract_features(code: str):
    """Very small AST-based feature extractor (placeholder).
    Returns a dict of numeric features.
    Handles syntax errors gracefully.
    """
    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        # Return default features for invalid syntax
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "syntax_error": str(e),
        }
    except Exception as e:
        # Handle other parsing errors
        return {
            "avg_func_len": 0,
            "loop_count": 0,
            "parse_error": str(e),
        }

    class Visitor(ast.NodeVisitor):
        def __init__(self):
            self.loop_count = 0
            self.func_lens = []

        def visit_FunctionDef(self, node):
            start = node.lineno
            end = getattr(node, 'end_lineno', node.lineno)
            self.func_lens.append(end - start + 1)
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
    }
