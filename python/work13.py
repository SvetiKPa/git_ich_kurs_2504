# Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
# Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
# Кортеж по возрастанию: (3, 7, 8, 10)
numbers = (3, 7, 2, 8, 5, 10, 1, 4, 15, 3, 7, 2, 8, 5, 10, 20)
a, *others = numbers
new_tuple = (a,)
max_value = numbers[0]
for i, value in enumerate(numbers):
#    print(i, numbers[i+1], new_tuple)
    if value > max_value:
        new_tuple += (value,)
        max_value = value
 #       max_value = max(value, numbers[i])
print("Кортеж по возрастанию: ", new_tuple)


#
#
# Повторяющиеся элементы
# Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. Вывести сами элементы и их индексы.
# Данные:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
new_numbers = ()
for ind, number in enumerate(numbers):
    a = numbers.count(number)
    indx = ()
#    print(new_numbers)
    if a > 1 and number not in new_numbers :
        new_numbers += (number,)
        for j, numm in enumerate(numbers):
            if number == numm:
                indx     += (j,)
        print(f"Индексы элемента {number}: ", *indx)

