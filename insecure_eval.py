def calculator(expr: str):
    # VULNERABILITY: eval on untrusted input
    return eval(expr)


if __name__ == "__main__":
    expr = input("Enter math expression: ")
    print(calculator(expr))


# SECURE VERSION: Safe mathematical expression evaluator
import ast
import operator

def calculator_secure(expr: str):
    """Safe alternative using AST validation and restricted operations."""
    try:
        node = ast.parse(expr, mode='eval')
        _validate_node(node.body)
        return _evaluate(node.body)
    except (ValueError, SyntaxError, TypeError) as e:
        raise ValueError(f"Invalid expression: {e}")

def _validate_node(node):
    """Whitelist allowed AST node types"""
    allowed_types = (ast.Constant, ast.BinOp, ast.UnaryOp, 
                     ast.Add, ast.Sub, ast.Mult, ast.Div, 
                     ast.Mod, ast.Pow, ast.UAdd, ast.USub)
    
    if not isinstance(node, allowed_types):
        raise ValueError(f"Operation not allowed")
    
    for child in ast.walk(node):
        if not isinstance(child, allowed_types):
            raise ValueError(f"Operation not allowed")

def _evaluate(node):
    """Safely evaluate validated AST node"""
    ops = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.Mod: operator.mod, ast.Pow: operator.pow,
        ast.UAdd: operator.pos, ast.USub: operator.neg,
    }
    
    if isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        return ops[type(node.op)](_evaluate(node.left), _evaluate(node.right))
    elif isinstance(node, ast.UnaryOp):
        return ops[type(node.op)](_evaluate(node.operand))
