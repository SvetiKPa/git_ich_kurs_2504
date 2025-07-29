-- 1. Выберите все строки из таблицы suppliers Предварительно подключитесь к базе данных northwind
USE northwind;
select * from suppliers;

-- 2. Выведите столбцы id, order_id из таблицы order_details, а также вычисляемый столбец category 
-- в зависимости от значений unit_price Если unit_price > 10 то значение столбца  category 'Expensive' 
-- В противном случае 'Cheap' Написать запрос двумя способами -  с применением операторов IF и CASE
select id, order_id,
case 
 when unit_price>10 then "Expensive"
 else "Cheap"
end as category
from northwind.order_details;

select id, order_id, if(unit_price>10, "Expensive", "Cheap") as category
from northwind.order_details;

-- 3. Вывести все строки там, где purchase_order_id не указано. 
-- При этом дополнительно создать столбец total_price как произведение quantity * unit_price
select quantity * unit_price as total_price from northwind.order_details where purchase_order_id is null;

-- 4. Вывести один столбец из таблицы employees содержащий имя и фамилию написанные через пробел 
-- Вывести 3 строки начиная со второй
select concat(first_name, " ",  last_name) from employees limit 3 offset 1; 
-- видимая первая строка - это нулевая.

-- 5. На основе таблицы orders вывести один столбец - с годом и месяцем из order_date в формате 'год-месяц'
select left(order_date, 7) from orders;

-- 6. Выведите уникальные имена компаний из таблицы customers Отсортируйте их по убыванию
select distinct company from customers order by company desc; 

-- 7. Отформатируйте стиль написания запросов
SELECT DISTINCT
    company
FROM
    customers
ORDER BY company DESC; 


-- 8. Сохраните запросы в виде файла с расширением .sql и загрузите на платформу
