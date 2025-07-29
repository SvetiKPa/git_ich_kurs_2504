# Реверс словаря
# Напишите программу, которая меняет местами ключи и значения в словаре. Если значения повторяются, добавьте их в список.
data = {"a": 1, "b": 2, "c": 1, "d": 3}
# Пример вывода:
# Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
inv_data = {}
for key, value in data.items():
    if value not in inv_data:
        inv_data[value] = [key]
    else :
        inv_data[value].append(key)
print("Перевернутый словарь: ", inv_data)


# Счётчик букв в словах
# Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь, где ключи — это слова,
# а значения — это ещё один словарь с подсчётом каждой буквы.
words = ["anna", "bennet", "john"]
# Пример вывода:
# {'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}
new_dict = {}
for word in words:
    dict2 = {w: word.count(w) for w in word }
    #print(dict2)
    new_dict[word] =  dict2
print(new_dict)


# Распределение студентов по группам
# У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен.
# Необходимо распределить студентов по группам:
# "Отличники": баллы >= 85
# "Хорошисты": баллы от 70 до 84
# "Троечники": баллы от 50 до 69
# "Не сдали": баллы < 50
# Создайте словарь с ключами-группами и словарями со студентами в качестве значений.
# Данные:
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
# Пример вывода:
# Распределение по группам:
# {'Отличники': {'Аня': 92, 'Дима': 88}, 'Хорошисты': {'Боря': 76}, 'Троечники': {'Ваня': 65, 'Ева': 54}, 'Не сдали': {'Галя': 48}}
new_dict_groups = {}
for group in groups:
    new_dict_groups.setdefault(group, {})
print(new_dict_groups)

for student, val in students.items():
#    print(student, val)
    if val >= 85:
        new_dict_groups["Отличники"][student] = val
    elif val >= 70 and val < 85:
        new_dict_groups["Хорошисты"][student] = val
    elif val >=50 and val < 70:
        new_dict_groups["Троечники"][student] = val
    else:
        new_dict_groups["Не сдали"][student] = val

print("Распределение по группам: ", new_dict_groups)

 #   dict_excel = {student: val for student, val in students.items() }
 #   dict_good  = {student: val for student, val in students.items() if val >= 70 and val < 85}
 #   dict3      = {student: val for student, val in students.items() if val >= 50 and val < 70}
 #   dict_not   = {student: val for student, val in students.items() if val < 50}


