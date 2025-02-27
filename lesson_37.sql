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
