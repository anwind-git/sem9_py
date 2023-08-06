from modal.equation import quadratic_equation
from modal.csv_decorator import quadratic_equation_decorator
from modal.csv_generator import generate_csv
from modal.json_decorator import save_results_to_json


generate_csv("random_numbers.csv", 5)


@quadratic_equation_decorator
@save_results_to_json
def calculate_roots(a, b, c):
    roots = quadratic_equation(a, b, c)
    return roots


calculate_roots("random_numbers.csv")
