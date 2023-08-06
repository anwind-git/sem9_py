import csv
import random
#Генерация csv файла с тремя случайными числами в каждой строке. 3 числа от 100 до 1000 в строке.
def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(num_rows):
            row = [random.randint(100, 1000), random.randint(100, 1000), random.randint(100, 1000)]
            writer.writerow(row)