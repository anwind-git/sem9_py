import json
"""
Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
"""
def save_results_to_json(func):
    def wrapper(a, b, c):
        roots = func(a, b, c)
        data = {"a": a, "b": b, "c": c, "roots": roots}
        with open("results.json", "a") as jsonfile:
            jsonfile.write(json.dumps(data) + "\n")
    return wrapper