import math

def predict_age(*args):
    total = sum(arg ** 2 for arg in args)
    
    return math.sqrt(total) // 2