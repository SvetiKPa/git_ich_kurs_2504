use northwind;
SELECT * FROM northwind.purchase_order_details;
-- 1. Для каждого заказа order_id выведите минимальный, максмальный и средний unit_cost
select purchase_order_id, min(unit_cost) over (partition by purchase_order_id) as minimum, 
max(unit_cost) over (partition by purchase_order_id) as maximum, 
avg(unit_cost) over (partition by purchase_order_id) as average 
from purchase_order_details;

-- 2.  Оставьте только уникальные строки из предыдущего запроса
select distinct purchase_order_id, min(unit_cost) over (partition by purchase_order_id) as minimum, 
max(unit_cost) over (partition by purchase_order_id) as maximum, 
avg(unit_cost) over (partition by purchase_order_id) as average 
from purchase_order_details;

select purchase_order_id, min(unit_cost), max(unit_cost), avg(unit_cost) 
from purchase_order_details group by purchase_order_id;


-- 3. Посчитайте стоимость продукта в заказе как quantity*unit_cost 
-- Выведите суммарную стоимость продуктов с помощью оконной функции Сделайте то же самое с помощью GROUP BY
select purchase_order_id, p.product_name, quantity*unit_cost , 
sum(quantity*unit_cost) over (partition by purchase_order_id) as summa_all 
from purchase_order_details
join products as p on p.id=purchase_order_details.product_id ;

select purchase_order_id, product_id, quantity*unit_cost , sum(quantity*unit_cost)  as summa_all 
from purchase_order_details
join products as p on p.id=purchase_order_details.product_id
group by purchase_order_id;

-- 4. Посчитайте количество заказов по дате получения и posted_to_inventory Если оно превышает 1 то выведите '>1' в противном случае '=1'
-- Выведите purchase_order_id, date_received и вычисленный столбец
select purchase_order_id, date_received,
case
when count(purchase_order_id) over (partition by date_received, posted_to_inventory)  >=1 then '>=1'
else "1"
end as orders
from purchase_order_details;

