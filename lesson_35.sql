-- Lesson 35. Первые запросы к базе данных Marvel
-- SELECT - это команда, которая позволяет выбирать данные из таблицы
-- FROM - команда указывающая на таблицу, из которой выбираются данные
-- WHERE - команда, которая позволяет фильтровать данные
-- LIMIT - команда, которая позволяет ограничить количество выбираемых строк
-- OFFSET - команда, которая позволяет пропустить определенное количество строк
-- Использование операторов сравнения (=, <, >, BETWEEN) и логических операторов (AND, OR, NOT)
-- DISTINCT - команда, которая позволяет выбрать уникальные значения
-- ORDER BY - команда, которая позволяет сортировать данные
-- LIKE - команда, которая позволяет искать строки, которые содержат определенный шаблон
-- IN - команда, которая позволяет выбрать строки, которые содержат одно из значений из списка

-- 1. ВЫБРАТЬ ВСЁ из таблицы MarvelCharacters
SELECT *
FROM MarvelCharacters;

-- 2. Выбрать name, appearances из таблицы MarvelCharacters
SELECT name, appearances
FROM MarvelCharacters;

-- ; - это разделитель запросов, чтобы можно было писать несколько запросов в одном файле

-- 3. Выбрать name, eye, где глаза Blue Eyes из таблицы MarvelCharacters
SELECT name, eye
FROM MarvelCharacters
WHERE eye = 'Blue Eyes';


-- 4. Выбрать name, eye, где глаза Blue Eyes И количество appearances больше 500 из таблицы MarvelCharacters
SELECT name, eye, appearances
FROM MarvelCharacters
WHERE eye = 'Blue Eyes' AND appearances > 500;

-- 5. Просто возьмем первые 5 записей
SELECT *
FROM MarvelCharacters
WHERE hair = "Bald"
LIMIT 5
OFFSET 5;

-- 6. Получим уникальный пол персонажей
SELECT DISTINCT SEX
FROM MarvelCharacters;


-- 7. Получим персонажей у которых пол Genderfluid Characters Agender Characters
SELECT name, SEX, appearances, year
FROM MarvelCharacters
WHERE SEX = "Genderfluid Characters" OR SEX = "Agender Characters"
ORDER BY appearances DESC
LIMIT 10;


SELECT name, SEX, appearances, year
FROM MarvelCharacters
WHERE SEX = "Genderfluid Characters" OR SEX = "Agender Characters"
ORDER BY appearances DESC
LIMIT 10;

-- 8. Два признака сортировки
SELECT name, SEX, appearances, year
FROM MarvelCharacters
WHERE SEX = "Genderfluid Characters"
    OR SEX = "Agender Characters" 
    AND appearances > 10
ORDER BY SEX, appearances DESC;

-- 9 Получим уникальный год, сортируем и получаем первую десятку
SELECT DISTINCT year
FROM MarvelCharacters
ORDER BY year
LIMIT 10;

-- 10. Мы увидели что минимальный год 1939 и можем посмотреть персонажей появившихся в период 1940 - 1945
SELECT name, year, appearances
FROM MarvelCharacters
WHERE year > 1939 
AND year < 1946
AND appearances > 20
ORDER BY appearances DESC;

-- 11. Такой же, но с использованием BETWEEN
SELECT name, year, appearances
FROM MarvelCharacters
WHERE year BETWEEN 1940 AND 1945
AND appearances > 20
ORDER BY appearances DESC;


-- 12. Поиск по шаблону
-- LIKE - ищет "похожие" строки
-- Шаблон - % - любое количество символов
-- Шаблон - _ - один символ
-- Шаблон - [abc] - один символ из набора ???
-- Шаблон - [a-z] - один символ из диапазона ???

--"Adolf%" - ищем строки начинающиеся с Adolf
-- "%man%" - вхождение man в любом месте внутри строки
SELECT name, year, appearances
FROM MarvelCharacters
WHERE name LIKE '% man %'
OR name LIKE '%-man %';

-- Выборка уникальных цветов глаз и волос
SELECT DISTINCT eye, hair
FROM MarvelCharacters;

-- Gold Eyes, Hazel Eyes, One Eye
-- Yellow Hair, Red Hair, No Hair
SELECT name, eye, hair, appearances
FROM MarvelCharacters
WHERE eye IN ('Gold Eyes', 'Hazel Eyes', 'One Eye')
AND hair IN ('Yellow Hair', 'Red Hair', 'No Hair');



