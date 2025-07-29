# Не уникальные числа
# Напишите программу, которая находит все числа, встречающиеся более одного раза в списке, и выводит их в порядке убывания.
# Пример вывода:
# Числа, встречающиеся более одного раза: [7, 4, 3, 8]
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
new_numbers = []
for i in numbers:
    if numbers.count(i) > 1 and i not in new_numbers:
        new_numbers.append(i)
new_numbers.sort(reverse=True)
print("Числа, встречающиеся более одного раза, в порядке убывания: ", new_numbers)

numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
new_numbers = {i for i in numbers if numbers.count(i) > 1 }
#print(new_numbers)
new_numbers = list(new_numbers)
new_numbers.sort(reverse=True)
print("Числа, встречающиеся более одного раза, в порядке убывания: ", new_numbers)



# Проверка подмножества Задача:
# Напишите программу, которая проверяет, является ли один словарь подмножеством другого (т.е. все его пары "ключ-значение" содержатся в другом словаре).
# Данные:
# Пример вывода:
# Первый словарь является подмножеством второго.
dict1 = {"a": 1, "g": 3}
dict2 = {"a": 1, "b": 2, "c": 3}

is_true = True
for key1 in dict1:
    if key1 not in dict2:
        is_true = False
        print(f"Ошибка: ключ '{key1}' отсутствует в dict2")
        break
    elif dict1[key1] != dict2[key1]:
        is_true = False
#    print(key1, dict2[key1], is_true)
print("Первый словарь является подмножеством второго", is_true)


