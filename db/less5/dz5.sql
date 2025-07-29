select * from northwind.purchase_order_details;
-- 1 Посчитайте основные статистики - среднее, сумму, минимум, максимум столбца unit_cost.
select avg(unit_cost) as avg, sum(unit_cost) as sum, min(unit_cost) as min, max(unit_cost) as max from northwind.purchase_order_details;

-- 2 Посчитайте количество уникальных заказов purchase_order_id
select count(distinct(purchase_order_id)) as count_purchase from northwind.purchase_order_details;

-- 3 Посчитайте количество продуктов product_id в каждом заказе purchase_order_id Отсортируйте полученные данные по убыванию количества
select count(product_id) as tovar from northwind.purchase_order_details group by purchase_order_id order by tovar desc;

-- 4 Посчитайте заказы по дате доставки date_received Считаем только те продукты, количество quantity которых больше 30
select count(date_received) from northwind.purchase_order_details where quantity > 30;

-- 5 Посчитайте суммарную стоимость заказов в каждую из дат Стоимость заказа - произведение quantity на unit_cost
select sum(quantity*unit_cost) as summa, date_received  from northwind.purchase_order_details where date_received is not null  group by date_received;

-- 6 Сгруппируйте товары по unit_cost и вычислите среднее и максимальное значение quantity только для товаров где purchase_order_id не больше 100
select avg(quantity), max(quantity), unit_cost from northwind.purchase_order_details where purchase_order_id<= 100  group by unit_cost;

-- 7 Выберите только строки где есть значения в столбце inventory_id Создайте столбец category - если unit_cost > 20 то 'Expensive' 
-- в остальных случаях 'others' Посчитайте количество продуктов в каждой категории
select sum(quantity) as kol, sum(quantity*unit_cost) as summa, sum(quantity*unit_cost)/sum(quantity) as avg_cena,
case 
when unit_cost > 20 then 'Expensive' 
else "-"
end as category
 from northwind.purchase_order_details where inventory_id is not null group by category;
