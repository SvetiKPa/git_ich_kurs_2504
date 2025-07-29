-- 1 Подключитесь к своей базе данных созданной на уроке
use 250425_Pakhomova;

/*2 Создайте таблицу, которая отражает погоду в Вашем городе за последние 5 дней и включает следующее столбцы
Id - первичный ключ, заполняется автоматически
Дата - не может быть пропуском
Дневная температура - целое число, принимает значения от -30 до 30
Ночная температура - целое число, принимает значения от -30 до 30
Скорость ветра - подумайте какой тип данных и ограничения необходимы для этого столбца */
create table if not exists weather (
	weather_id int primary key auto_increment,
    `date` date not null,
    daytemp tinyint check(daytemp >-30 and daytemp < 30), 
    nigthtemp tinyint check(nigthtemp >-30 and nigthtemp < 30), 
    speed decimal(5, 2) check(speed >= 0)
);

/*3 Заполните таблицу 5 строками - за последние 5 дней */
insert into 250425_Pakhomova.weather
	(date, daytemp, nigthtemp, speed) 
values 
	(date_sub(current_date, interval 4 day) , 18, 12, 11.50), 
	(date_sub(current_date, interval 3 day) , 13, 8,  13.00), 
	(date_sub(current_date, interval 2 day) , 16, 12, 10.00), 
	(date_sub(current_date, interval 1 day) , 15, 9,  5.50), 
	(date_sub(current_date, interval 0 day) , 19, 15, 2.50)
;

-- 4 Увеличьте значения ночной температуры на градус если скорость ветра не превышала 3 м/с
set sql_safe_updates = 0;
update 250425_Pakhomova.weather set nigthtemp = nigthtemp +1 where speed <= 3;

/*5 На основе полученной таблицы создайте представление в своей базе данных - включите все строки Вашей таблицы и дополнительно рассчитанные столбцы
Средняя суточная температура - среднее арифметическое между ночной и дневной температурами
Столбец на основе скорости ветра - если скорость ветра не превышала 2 м/с то 
значение ‘штиль’, от 2 включительно до 5 - ‘умеренный ветер’, в остальных случаях 
- ‘сильный ветер’
6 Отформатируйте стиль написания запросов
7 Сохраните запросы в виде файла с расширением .sql и загрузите на платформу*/
create view view_new as
select * ,
(daytempview_new+nigthtemp)/2 as sred,
case 
	when speed < 2 then "штиль"
    when speed >=2 and speed < 5 then "умеренный ветер"
    else "сильный ветер"
end as wind
from weather;

select* from view_new;

