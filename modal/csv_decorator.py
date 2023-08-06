import csv
"""
Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
"""
def quadratic_equation_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                a, b, c = map(int, row)
                roots = func(a, b, c)
    return wrapper