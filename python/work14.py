# Число в конце
# Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка,
# в которых цифры находятся только в конце.
# Данные:
# # Пример вывода:
# Строки с цифрами только в конце: ['apple23', 'grape3']

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_list = []
for word in strings:
    without = word.rstrip('1234567890')
    if without.isalpha():
        new_list.append(word)
print("Строкa с цифрами только в конце: ", new_list)



# Удаление кратных
# Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
# Введите число для удаления кратных ему элементов: 3
# Список без кратных значений: [1, 10, 19, 20]
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
#a = int(input("Введите число для удаления кратных ему элементов: "))
a = 3
# new_list = []      #новый лист
# for i in numbers:
#     if i % a != 0:
#         new_list.append(i)
# print(f"Список без кратных {a}-м значений (append): ", new_list)

#remove изменяет кол-во эл-в
for j in numbers[::-1]:
    if j % a == 0:
        numbers.remove(j)
#        print("len", len(numbers))
print(f"Список без кратных {a}-м значений (remove): ", numbers)



# Порядок четных
# Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
# нечетные числа занимают те же позиции,
# чётные числа отсортированы между собой обратном порядке.
# Пример вывода:
# Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]
# Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7, 6]
new_numbers = []
for i in numbers:
    if i % 2 == 0:
        new_numbers.append(i)
new_numbers.sort()
#print("new", new_numbers)

output_list = []
for j in numbers:
    if j % 2 == 0:
#        numbers.pop()
        output_list.append(new_numbers.pop())
    else:
        output_list.append(j)

print("Список после сортировки: ", output_list)
