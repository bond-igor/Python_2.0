
import csv
import json
import random
import math
import functools

def generate_csv_file(filename, rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(rows):
            writer.writerow([random.randint(1, 100) for _ in range(3)])

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def save_to_json(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = []
        with open(args[0], 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result.append({'param': [a, b, c], 'result': func(a, b, c)})
        with open('results.json', 'w') as f:
            json.dump(result, f)
    return wrapper

# Нахождение корней квадратного уравнения
@save_to_json
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = (x1, x2)
    elif discriminant == 0:
        result = (-b / (2 * a))
    else:
        result = None
    return result
