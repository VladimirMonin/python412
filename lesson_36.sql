-- 25.02.2025
-- Тема SQL. Ч2. Подзапросы. Знакомство с GROUP BY. Урок: 36

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

-- Подзапросы, возможность делать запрос в запросе.

-- Сортируем базу по appearances. Выводим цвета глаз берем название цвета глаз (первое попавшееся) и выводим 
-- всех персонажей с этим цветом глаз.

-- Это можно сделать в два запроса

-- Цвета глаз
SELECT EYE
FROM MarvelCharacters
ORDER BY APPEARANCES DESC
LIMIT 1;

-- Персонажи с цветом глаз
SELECT name, EYE, appearances, Year
FROM MarvelCharacters
WHERE EYE = 'Hazel Eyes';
ORDER BY YEAR DESC, APPEARANCES DESC;


-- В одном запросе с использованием подзапроса
SELECT name, EYE, appearances, Year
FROM MarvelCharacters
WHERE EYE = (
    SELECT EYE
    FROM MarvelCharacters
    ORDER BY APPEARANCES DESC
    LIMIT 1
)
ORDER BY YEAR DESC, APPEARANCES DESC;


--TODO Найдите в подзапросе самого популярного (APPEARANCES) персонажа с Secret Identity
-- Выведите всех персонажей появившихся в том же году, что и самый популярный персонаж с Secret Identity

SELECT name, APPEARANCES, Year, identify
FROM MarvelCharacters
WHERE Year = (
    SELECT Year
    FROM MarvelCharacters
    WHERE identify = 'Secret Identity'
    ORDER BY APPEARANCES DESC
    LIMIT 1
);

-- DISTINCT - уникальные значения
SELECT DISTINCT Hair,
FROM MarvelCharacters
WHERE Hair IS NOT NULL;

-- GROUP BY - группировка
SELECT Hair,
FROM MarvelCharacters
WHERE Hair IS NOT NULL
GROUP BY Hair;


-- Count - количество
SELECT Hair, Count(*)
FROM MarvelCharacters
WHERE Hair IS NOT NULL
GROUP BY Hair;

-- Давайте сделаем похожую выборку по столбцу identify

SELECT identify, Count(*) AS total
FROM MarvelCharacters
GROUP BY identify
ORDER BY total DESC;

-- Сортировка по полу
SELECT Sex, Count(*) AS total
FROM MarvelCharacters
GROUP BY Sex;

-- Сделаем это же, но добудем самых популрных в каждой группе
SELECT Sex, Count(*) AS total, Max(appearances) AS max_appearances, name
FROM MarvelCharacters
GROUP BY Sex;

-- Группировка цвет глаз и персонажи с максимальным количеством появлений
SELECT EYE, Min(appearances), Sum(appearances), Max(appearances), name
FROM MarvelCharacters
GROUP BY EYE
HAVING Max(appearances) > 100;

-- при наличии min и max по одному столбцу, NAME будет выведен той позиции, которая последняя в запросе