def arithmetic(a, b, operator):
    operators = {
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "divide": lambda a, b: a / b,
        "multiply": lambda a, b: a * b
    }
    
    return operators[operator](a, b)