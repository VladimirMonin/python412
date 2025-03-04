-- Lesson 38
-- Create
-- Delete
-- Update


-- DDL MarvelCharacters
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


-- Операция создания. Create
-- Оператор INSERT

INSERT INTO MarvelCharacters (name)
VALUES ('Potato-Man');

SELECT * FROM MarvelCharacters
WHERE name LIKE '%Potato%';

-- Операция Update
-- Оператор UPDATE

UPDATE MarvelCharacters
SET year = 2025, hair = 'blond', alive = 'yes'
WHERE name like '%Potato%';

-- Сделаем выборку ID подзапросом, и у одного из них обновим данные
UPDATE MarvelCharacters
SET year = 2026, hair = 'bolt', alive = 'no', name = 'Potato-Woman'
WHERE ID = (
    SELECT ID
    FROM MarvelCharacters
    WHERE name LIKE '%Potato%'
    LIMIT 1
);

-- Операция Delete
-- Оператор DELETE

DELETE FROM MarvelCharacters
WHERE name LIKE '%Potato%';

SELECT * FROM MarvelCharacters
WHERE name LIKE '%Potato%';
