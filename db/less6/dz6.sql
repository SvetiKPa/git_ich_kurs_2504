SELECT * FROM northwind.orders;
select * from northwind.purchase_orders;
-- 1 Выведите одним запросом с использованием UNION столбцы id, employee_id из таблицы orders и соответствующие им столбцы из таблицы purchase_orders 
-- В таблице purchase_orders  created_by соответствует employee_id   
select id, employee_id as new_empl from northwind.orders 
union all
select id, created_by as new_empl from northwind.purchase_orders;

-- 2 Из предыдущего запроса удалите записи там где employee_id не имеет значения Добавьте дополнительный 
-- столбец со сведениями из какой таблицы была взята запись
select id, employee_id as new_empl, 'orders' from northwind.orders where employee_id is not null
union
select id, created_by as new_empl, 'purchase_orders' from northwind.purchase_orders where created_by is not null;

-- 3 Выведите все столбцы таблицы order_details а также дополнительный столбец payment_method из таблицы purchase_orders 
-- Оставьте только заказы для которых известен payment_method
select o.* , payment_method, purchase_orders.id
from order_details as o
inner join purchase_orders
on o.purchase_order_id=purchase_orders.id
where payment_method is not null;

-- 4 Выведите заказы orders и фамилии клиентов customers для тех заказов по которым были инвойсы таблица invoices
SELECT invoice_date, order_id, customer_id, concat(last_name, '  ', first_name) as FIO  
FROM northwind.invoices
inner join northwind.orders
on invoices.order_id = orders.id
join northwind.customers
on orders.customer_id=customers.id;

-- 5 Подсчитайте количество инвойсов для каждого клиента из предыдущего запроса*/
SELECT count(invoice_date) as count, concat(last_name, '  ', first_name) as FIO
FROM northwind.invoices
join northwind.orders
on invoices.order_id = orders.id
join northwind.customers
on orders.customer_id=customers.id
group by customer_id;
