use northwind;

-- 1. Выберите все строки из таблицы suppliers. Предварительно подключитесь к базе данных northwind
SELECT * FROM northwind.suppliers;

-- 2. Выберите только те строки из таблицы suppliers где company имеет значение Supplier A
-- 3. Выберите все строки из таблицы purchase_orders
-- 4. Выберите только те строки из таблицы purchase_orders  где supplier_id = 2
-- 5. Выберите supplier_id и shipping_fee из purchase_orders там где created_by равно 1 и supplier_id равен 5 Объясните полученный результат
-- 6. Выберите last_name и first_name из таблицы employees
-- там где адрес address имеет значение 123 2nd Avenue или 123 8th Avenue
-- Напишите запрос двумя способами - с применением оператора OR и оператора IN
-- 7. Выведите все имена сотрудников, которые содержат английскую букву p в середине фамилии
-- 8. Выберите все строки из таблицы orders там где нет информации о  shipper_id
-- 9. Отформатируйте стиль написания запросов
-- 10. Сохраните запросы в виде файла с расширением .sql и загрузите на платформу
select * from northwind.suppliers where company = 'Supplier A';
select * from purchase_orders;
select * from purchase_orders where supplier_id = 2;
select supplier_id, shipping_fee from northwind.purchase_orders where created_by = 1 and supplier_id = 5;
select last_name, first_name from northwind.employees where address in ('123 2nd Avenue', '123 8th Avenue');
select last_name, first_name from northwind.employees where address = '123 2nd Avenue' or address ='123 8th Avenue';
SELECT 
    first_name
FROM
    northwind.employees
WHERE
    last_name LIKE ('%p%');
SELECT 
    *
FROM
    northwind.orders
WHERE
    shipper_id IS NULL;
    
--  запросы не "читаюся", если их форматировать ))) 