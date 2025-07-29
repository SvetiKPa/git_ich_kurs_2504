# 1. Объединение данных в строку
# Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) и возвращает их строковое
# представление, объединённое через " | ". Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
# Пример вывода:
# 42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}
#list[Any]
#join.map()

#d1 = " | ".join(map(str, data))
#print(d1)
from typing import Any
def concat_any(data: list[Any]) -> str:
    """
    Объединяет данные в строковое представление через разделитель ' | '.
    :param data: Список данных любого типа.
    :return: Строка с объединёнными данными.
    """
    d1 = " | ".join(map(str, data))
    return d1
print(concat_any(data))


# 2. Сумма вложенных чисел
# Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и список баллов.
# Функция должна вернуть сумму всех чисел. Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
# Данные:
data = [
    {"name": "Alice", "scores": [10, 20, 30.5]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]
# Пример вывода:
# Итоговый балл: 156

from functools import reduce
#all_sc = (map(lambda item: item["scores"], data))
#list2 = reduce(lambda x, y: x + y, all_sc)
#print(list2)

def sum_notes_dict(list1: list[dict[str, str] | dict[float]]) -> float:
    """
    Вычисляет сумму всех чисел в списках внутри словарей.
    :param data: Список словарей, где каждый словарь содержит имя и список чисел.
    :return: Сумма всех чисел.
    """
    iter1 = map(lambda item: item["scores"], list1)
    a = sum(reduce(lambda x, y: x + y, iter1))
    return a

print(sum_notes_dict(data))


