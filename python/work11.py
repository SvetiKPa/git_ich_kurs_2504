# # Звёздочки вместо чисел
# # Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# # text = "My number is 123-456-789"
text = "My number is 123-456-789"
new_text = ''
for i in text:
#    if i.isdigit() == 0: new_text += i
#    else: new_text += '*'
    if not i.isdigit() : new_text += i
    else: new_text += '*'
#или replace
print(new_text)
#
# Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
# с указанием их количества. Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# имвол 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)

text = "Programming in python"
text = text.lower()
new_text = ''
for i in text:
    if i not in new_text:
        if text.count(i) > 1:
            count = text.count(i)
            print('Символ ', i, ' встречается ', count, ' раз(а)' )
        new_text += i
#        print(new_text)


# # Увеличение чисел
# # Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# # text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# # Пример вывода:
# # I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words = text.split(' ')
#new_text = ''
for i in range(len(words)):
   if words[i].count(".") < 2 and words[i].replace(".", "").isdecimal():
        words[i] = str(float(words[i]) * 10)

new_text = " ".join(words)
print(new_text)

