use northwind; 
SELECT * FROM northwind.products;
/*1   Вывести названия продуктов таблица products, включая количество заказанных единиц quantity 
для каждого продукта таблица order_details.
Решить задачу с помощью cte и подзапроса*/

select product_id,  product_name, quant
from products 
left join  
	(select product_id, sum(quantity) as quant 
    from order_details 
    group by product_id) as order_q
on products.id=order_q.product_id;

with orders_quantity as 
	(SELECT product_id, SUM(quantity) as quant 
    FROM order_details 
    GROUP BY product_id)
SELECT id, product_name, quant
FROM products 
LEFT JOIN orders_quantity 
ON products.id = orders_quantity.product_id;


-- 2  Найти все заказы таблица orders, сделанные после даты самого первого заказа клиента Lee таблица customers.
with first_ord_lee as (
	select order_date from orders where orders.customer_id in (select id from customers where last_name='Lee') order by order_date limit 1)
select * from orders where order_date > (select order_date from first_ord_lee) ;


-- 3 Найти все продукты таблицы  products c максимальным target_level
select * from products where target_level = (select max(target_level) from products);

WITH max_level as
	(SELECT MAX(target_level) as ml FROM products)
SELECT * 
FROM products 
WHERE target_level = 
	(SELECT ml from max_level);
