# Сумма цифр числа
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
num = -43197.5
# 24
def sum_nummers_nummer1(f: float) -> int:
    """
    Сумма цифр числа
    :param f: float
    :return: int
    """
    sum = 0
    f = str(abs(f)).replace(".", "")
    for i in f:
        sum += int(i)
    return sum
print("not recursive", sum_nummers_nummer1(num))

def sum_nummers_nummer_rec(f: float) -> int:
    s = str(abs(f)).replace(".", "")
    if len(s) == 1:
        return int(s)
    return int(s[0]) + sum_nummers_nummer_rec(float(s[1:]))
print("recursive", sum_nummers_nummer1(num))

#
# Сумма вложенных чисел
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
nested_numbers = [1, [2, 3], [4, [5, 6], 9.5], 7]
# Пример вывода:
# 28

def sum_numers_list(list1: list[int, list[float]]) -> float:
    """
    Сумма вложенных чисел (во вложенных списках)
    :param list1: разный уровень вложенности
    :return: float
    """
    sum = 0
    for item in list1:
        if isinstance(item, (int, float)):
            sum += item
        elif isinstance(item, list):
            sum += sum_numers_list(item)
    return sum


print(sum_numers_list(nested_numbers))
