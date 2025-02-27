-- План занятия: Агрегатные функции и Common Table Expressions (WITH)
-- CRUD 
-- Create
-- Read
-- Update
-- Delete

-- 1. Расширенная работа с агрегатными функциями
--    1.1. Повторение базовых агрегатных функций (COUNT, SUM, MIN, MAX, AVG)
--    1.2. GROUP BY с несколькими столбцами
--    1.3. HAVING для продвинутой фильтрации агрегированных данных
--    1.4. Вложенные агрегатные функции
--
-- 2. Common Table Expressions (WITH)
--    2.1. Основы использования WITH
--    2.2. Улучшение читаемости сложных запросов
--    2.3. Многократное использование CTE в одном запросе
--    2.4. Рекурсивные CTE (базовое знакомство)
--
-- 3. Комбинирование WITH и агрегатных функций
--    3.1. Создание временных наборов данных для дальнейшей агрегации
--    3.2. Многоуровневая агрегация через несколько CTE
--
-- 4. Практические задачи
--    4.1. Анализ популярности персонажей по годам появления
--    4.2. Сравнение групп персонажей по различным характеристикам
--    4.3. Поиск корреляций между атрибутами персонажей

-- DDL
-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identify         TEXT,
--     ALIGN            TEXT,
--     EYE              TEXT,
--     HAIR             TEXT,
--     SEX              TEXT,
--     GSM              TEXT,
--     ALIVE            TEXT,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER
-- );


-- 1. Получим уникальные цвета глаз 
SELECT DISTINCT eye
FROM MarvelCharacters

-- 2. Сколько всего уникальных цветов глаз?
SELECT count(DISTINCT eye)
FROM MarvelCharacters

-- 3. Max appearances
SELECT name, eye, max(appearances)
FROM MarvelCharacters

-- 3. Min year
SELECT name, min(year)
FROM MarvelCharacters

-- 4. Группы по цветам глаз
SELECT eye
FROM MarvelCharacters
GROUP BY eye

-- 5. Среднее количество появлений по группам цвета глаз
SELECT eye, round(avg(appearances), 2) as avg_app
FROM MarvelCharacters
WHERE eye is not NULL
GROUP BY eye
HAVING avg_app > 10
ORDER BY avg_app DESC

-- 6. Имена персонажей с количеством появлений больше чем среднее
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances > (
    SELECT avg(appearances) 
    FROM MarvelCharacters
    )
ORDER BY appearances DESC

--

WITH AverageAppearances AS (
    SELECT avg(appearances) AS avg_count
    FROM MarvelCharacters
)
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances > (SELECT avg_count FROM AverageAppearances)
ORDER BY appearances DESC

--

WITH AverageAppearances AS (
    SELECT avg(appearances) AS avg_count
    FROM MarvelCharacters
)
SELECT name, appearances
FROM MarvelCharacters, AverageAppearances
WHERE appearances > avg_count
ORDER BY appearances DESC

-- WITH готовим данные - name not like %(Earth-616)
--
WITH Alians AS (
    SELECT *
    FROM MarvelCharacters
    WHERE name NOT LIKE '%(Earth-616)'
    AND name LIKE '%Earth%'
)
SELECT name, appearances FROM Alians


-- COUNT - SUM - MIN - MAX - AVG

-- Задача 1
-- Найдите среднее количество появлений персонажей Marvel для каждого пола (SEX) и отсортируйте результаты по убыванию среднего значения.

SELECT sex, round(avg(appearances), 2) AS avg_app
FROM MarvelCharacters
WHERE sex is not NULL
GROUP BY sex
ORDER BY avg_app DESC



-- Задача 2
-- Определите, сколько персонажей Marvel с каждым цветом волос (HAIR) появилось в каждом десятилетии (используйте деление года на 10 и умножение на 10 для определения десятилетия).


SELECT 
    HAIR,
    (Year / 10) * 10 AS decade,
    COUNT(*) AS character_count
FROM MarvelCharacters
WHERE HAIR IS NOT NULL
AND decade IS NOT NULL
GROUP BY HAIR, decade
ORDER BY decade, character_count DESC;


-- Задача 3. Сделаем декады, сгруппируемся по ним и вывыдем самого популярного персонажа декады
SELECT (Year / 10) * 10 AS decade, name, max(appearances)
FROM MarvelCharacters
WHERE year is not null and decade is not null
GROUP BY decade
ORDER BY decade

-- Задача 4. Для мировозрения выведем лидера и год появления
SELECT name, year, ALIGN, max(appearances) as max_app
FROM MarvelCharacters
WHERE ALIGN is not NULL
GROUP BY ALIGN
ORDER BY max_app DESC



WITH AlignGroup AS (
    SELECT *
    FROM MarvelCharacters
    WHERE ALIGN is not NULL
    GROUP BY ALIGN
)
-- ) максимальное, минимальное и среднее количество появлений персонажей.
SELECT MAX(appearances) AS max_app,
MIN(appearances) AS min_app,
ROUND(AVG(appearances), 2) AS avg_app
FROM AlignGroup

-- Первые JOIN запросы. 
-- name, year, appearances из MarvelCharacters
-- color из EyeColor

SELECT MarvelCharacters.name, MarvelCharacters.year, MarvelCharacters.appearances, EyeColor.color
FROM MarvelCharacters
JOIN EyeColor ON MarvelCharacters.eye_id = EyeColor.eye_id


SELECT mc.name, mc.year, mc.appearances, ec.color, hc.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id


SELECT mc.name, mc.year, mc.appearances, ec.color, hc.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
JOIN HairColor AS hc ON mc.hair_id = hc.hair_id

WHERE ec.color = 'Blue Eyes' AND hc.color = 'Blond Hair'


--
SELECT mc.name, mc.year, mc.appearances, ec.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id