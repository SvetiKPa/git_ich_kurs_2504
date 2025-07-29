use northwind;
SELECT * FROM northwind.order_details;
-- 1 Для каждого product_id выведите inventory_id а также предыдущий и последующей inventory_id по убыванию quantity
SELECT product_id, quantity, inventory_id, lead(inventory_id) over (partition by product_id order by quantity desc) as lead_invent, 
lag(inventory_id) over (partition by product_id order by quantity desc) as lag_invent
FROM northwind.order_details;

-- 2 Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST VALUE  Вывести order_id и полученные значения
select distinct order_id,  first_value(unit_price) over (partition by order_id order by unit_price) as min_price, 
first_value(unit_price) over (partition by order_id order by unit_price desc) as max_price
FROM northwind.order_details;

-- 3 Выведите order_id и столбец с разнице между  unit_price для каждой заказа и минимальным unit_price в рамках одного заказа 
-- Задачу решить двумя способами - с помощью First VAlue и MIN

select order_id, unit_price, (unit_price- first_value(unit_price) over (partition by order_id order by unit_price )) as diff_price
FROM northwind.order_details;

SELECT order_id, unit_price, unit_price - MIN(unit_price) OVER (PARTITION BY order_id) as diff_price
FROM northwind.order_details;

-- 4 Присвойте ранг каждой строке используя RANK по убыванию quantity
select *, rank() over (order by quantity desc) as rnk, 
row_number() over (order by quantity desc) as nn
FROM northwind.order_details;

-- 5  Из предыдущего запроса выберите только строки с рангом до 10 включительно
select *, rank() over (order by quantity desc) as rnk, 
row_number() over (order by quantity desc) as nn
FROM northwind.order_details
limit 10;


select * 
from (select *,  rank() over (order by quantity desc) as rnk, 
row_number() over (order by quantity desc) as nn
FROM northwind.order_details ) as subqw
where  rnk<=10;


WITH ranked_orders AS (
    SELECT *, 
           RANK() OVER (ORDER BY quantity DESC) AS rnk
    FROM northwind.order_details
)
SELECT *
FROM ranked_orders
WHERE rnk <= 10;


