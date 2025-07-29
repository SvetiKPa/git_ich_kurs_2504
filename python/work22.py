# 1. Выбор заказов
# У вас есть список заказов. Каждый заказ содержит название продукта и его цену.
# Напишите функцию, которая:
# Отбирает заказы дороже 500. Создаёт список названий отобранных продуктов в алфавитном порядке.
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]
# Пример вывода: ['Chair', 'Laptop']

def sorted_products1(list1):
    result = filter(lambda item: item["price"] > 500, orders)
    #print(list(result), "111")
    return sorted(map(lambda item: item["product"], result))
    #print(list(result1), "222")

print("sorted_products1", sorted_products1(orders))


def sorted_product(list1) :
    for item in list1:
        list2 = [item["product"] for item in list1 if item["price"] > 500]
        return sorted(list2)

print("sorted_product", sorted_product(orders))

# 2. Статистика продаж
# Дан список продаж в виде кортежей (товар, количество, цена).
# Напишите программу, которая:
# Вычисляет общую выручку для каждого товара.
# Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.
# Данные:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]
# Пример вывода:
# {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}
def sum_sales(list1):
    dict1 = {}
    for name, q, pr in list1:
        dict1[name] = q * pr
#    print(dict1)
    return dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
#    return sorted_items
print("111", sum_sales(sales))


def sum_sales1(list1):
    result = sorted(map(lambda item: (item[0], item[1]*item[2]), sales ), key=lambda item: item[1], reverse=True)
    return dict(result)

print("222", sum_sales1(sales))
