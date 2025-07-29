# Одно слово
# Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
# Пример вывода:
# Обработанный список: ['hello', 'world', 'simple']

text_list = ["Hello", "Python Programming", "a World", "Advanced Topics", "Simple"]
for i in range(len(text_list)-1, -1, -1):
    if text_list[i].find(" ") > 0: del text_list[i]
    else: text_list[i] = text_list[i].lower()
print(text_list)

# Обновление цен товаров
# Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
# Пример вывода:
# Введите скидку (в процентах): 17
# Товар          Старая цена    Новая цена
# Laptop            1200.00$       996.00$
# Mouse                25.00$         20.75$
# Keyboard           75.00$         62.25$
# Monitor            200.00$       166.00$
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#a = float(input(" Введите скидку (в процентах): "))
a = 10.5
print("Товар               Старая цена    Новая цена")
for product in products:
    name, price = product
    new_price = price * (1 - a/100.0)
    product.append(new_price)
    print(f"{name:<20} {price:10.2f}$ {new_price:10.2f}$ ")
print(products)
