-- 1. Выведите Ваш возраст на текущий день в секундах
SELECT TIMESTAMPDIFF(HOUR, '2014-04-04 16:40:00', NOW())*3600 as secund, now();

-- 2. Выведите какая дата будет через 51 день
SELECT DATE_ADD(NOW(), INTERVAL 51 DAY);

-- 3. Отформатируйте предыдущей запрос - выведите день недели для этой даты Используйте документацию My SQL
SELECT DATE_FORMAT(DATE_ADD(NOW(), INTERVAL 51 DAY), '%W') AS dayofweek;

-- 4.  Подключитесь к базе данных northwind Выведите столбец с исходной датой создания транзакции 
-- transaction_created_date из таблицы inventory_transactions, 
SELECT 
    transaction_created_date
FROM
    northwind.inventory_transactions;

-- а также столбец полученный прибавлением 3 часов к этой дате
select DATE_ADD(transaction_created_date, INTERVAL 3 HOUR) as plus_3 from northwind.inventory_transactions;


-- 5. Выведите столбец с текстом  'Клиент с id <customer_id> сделал заказ <order_date>' из таблицы orders
-- Запрос написать двумя способами - с использованием неявных преобразований а также с указанием изменения типа данных для столбца customer_id
-- Внимание В MySQL функция CAST не принимает VARCHAR в качестве параметра для длины. Вместо этого, нужно использовать CHAR для указания длины.
select concat("Клиент c id ", customer_id, " сделал заказ ", order_date ) as text , customer_id, order_date from northwind.orders;
select concat("Клиент c id ", cast(customer_id as char), " сделал заказ ", cast(order_date AS char)) as text , customer_id, order_date from northwind.orders;


