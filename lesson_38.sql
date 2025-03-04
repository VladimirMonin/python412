-- Lesson 38
-- Create
-- Delete
-- Update


-- DDL Базы Marvel Normal

-- CREATE TABLE MarvelCharacters (
--     id               INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id          INTEGER,
--     name             TEXT,
--     urlslug          TEXT,
--     identity_id      INTEGER,
--     align_id         INTEGER,
--     eye_id           INTEGER,
--     hair_id          INTEGER,
--     sex_id           INTEGER,
--     status_id        INTEGER,
--     APPEARANCES      INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year             INTEGER,
--     FOREIGN KEY (
--         identity_id
--     )
--     REFERENCES Identity (identity_id),
--     FOREIGN KEY (
--         align_id
--     )
--     REFERENCES Alignment (align_id),
--     FOREIGN KEY (
--         eye_id
--     )
--     REFERENCES EyeColor (eye_id),
--     FOREIGN KEY (
--         hair_id
--     )
--     REFERENCES HairColor (hair_id),
--     FOREIGN KEY (
--         sex_id
--     )
--     REFERENCES Sex (sex_id),
--     FOREIGN KEY (
--         status_id
--     )
--     REFERENCES LivingStatus (status_id) 
-- );

-- -- Посмотрим все цвета глаз
-- SELECT * FROM EyeColor

-- -- id 2 Blue Eyes

-- -- Вставка данных
-- INSERT INTO MarvelCharacters
-- (name, eye_id)
-- VALUES ('CatMan', 2);

-- -- Выборка данных
-- SELECT * FROM MarvelCharacters
-- WHERE name LIKE '%CatMan%';


-- Как это сделать в один запрос?

INSERT INTO MarvelCharacters
(name, eye_id)
VALUES (
    "CatWoman",
    (
        SELECT eye_id
        FROM EyeColor
        WHERE color LIKE 'Blue%'
    )
)

SELECT * FROM MarvelCharacters
WHERE name LIKE 'Cat%';


-- Проверим цвет глаз персонажа через JOIN
SELECT mc.name, ec.color
FROM MarvelCharacters AS mc
JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
WHERE name LIKE 'Cat%';

-- У нас возник дубль CatWoman без указанного цвета глаз
-- Давайте укажем ей Amber Eyes

UPDATE MarvelCharacters
SET eye_id = (
    SELECT eye_id
    FROM EyeColor
    WHERE color = "Amber Eyes"
)
WHERE name = "CatWoman" AND eye_id IS NULL

-- Удалим созданных персонажей через IN
DELETE FROM MarvelCharacters
WHERE name IN ('CatMan', 'CatWoman')


-- Сделам сводную таблицу через WITH 
-- Чтобы там были персонажи со всеми данными а так же ID
WITH MarvelCharactersFull AS (
    SELECT mc.*, id.identity AS identity_name, al.name AS align_name, ec.color AS eye_color, hc.color AS hair_color, s.name AS sex_name, ls.status AS status_name
    FROM MarvelCharacters AS mc
    JOIN Identity AS id ON mc.identity_id = id.identity_id
    JOIN Alignment AS al ON mc.align_id = al.align_id
    JOIN EyeColor AS ec ON mc.eye_id = ec.eye_id
    JOIN HairColor AS hc ON mc.hair_id = hc.hair_id
    JOIN Sex AS s ON mc.sex_id = s.sex_id
    JOIN LivingStatus AS ls ON mc.status_id = ls.status_id
)
SELECT * FROM MarvelCharactersFull


-- Используем эту заготовку для создания персонажа с цветом Brown Eyes и White Hair
