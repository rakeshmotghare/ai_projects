
def calculator(expression: str) -> str:
    '''Evaluate a mathematical expression and return the result as a string.'''
    allowed_chars = "0123456789+-*/(). "
    if not all(c in allowed_chars for c in expression):
        return "Invalid characters in expression."
    try:
        # Evaluate the expression safely
        return str(eval(expression))
    except Exception as exc:
        return f"Error evaluating expression: {exc}"