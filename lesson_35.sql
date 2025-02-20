-- Lesson 35. Первые запросы к базе данных Marvel
-- SELECT - это команда, которая позволяет выбирать данные из таблицы
-- FROM - команда указывающая на таблицу, из которой выбираются данные
-- WHERE - команда, которая позволяет фильтровать данные
-- LIMIT - команда, которая позволяет ограничить количество выбираемых строк
-- OFFSET - команда, которая позволяет пропустить определенное количество строк
-- Использование операторов сравнения (=, <, >, BETWEEN) и логических операторов (AND, OR, NOT)
-- DISTINCT - команда, которая позволяет выбрать уникальные значения
-- ORDER BY - команда, которая позволяет сортировать данные

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
LIMIT 10


SELECT name, SEX, appearances, year
FROM MarvelCharacters
WHERE SEX = "Genderfluid Characters" OR SEX = "Agender Characters"
ORDER BY appearances DESC
LIMIT 10

-- 8. Два признака сортировки
SELECT name, SEX, appearances, year
FROM MarvelCharacters
WHERE SEX = "Genderfluid Characters"
    OR SEX = "Agender Characters" 
    AND appearances > 10
ORDER BY SEX, appearances DESC
