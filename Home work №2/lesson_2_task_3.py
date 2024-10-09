import math

def square(side):
    if side.is_integer():
        side = math.ceil(side)
    
    return side * side


side_length = float(input("Введите длину стороны квадрата: "))
result = square(side_length)
print(f"Площадь квадрата: {result}")
