-- План занятия №40: Транзакции и триггеры в SQLite
-- Повторение материала урока 39

-- Структура созданных таблиц (Students, Groups, StudentCards, Teachers, GroupsTeachers)
-- Типы связей между таблицами
-- Особенности работы с внешними ключами
-- Теория транзакций

-- Что такое ACID
-- A - Atomicity (Атомарность)
-- C - Consistency (Согласованность)
-- I - Isolation (Изолированность)
-- D - Durability (Долговечность)
-- Зачем нужны транзакции
-- Когда использовать транзакции
-- Принцип "всё или ничего"
-- Триггеры

-- Индексы и их типы в SQLite

-- Простой индекс (Single-Column)

    -- Самый распространенный
    -- Для полей, по которым часто ищут (например, email, телефон, фамилия)
    -- Когда делаете WHERE по одному полю

-- Уникальный индекс (UNIQUE)

    -- Когда нужно запретить дубли
    -- Для бизнес-ключей (номера документов, логины)
    -- Автоматом создаётся на PRIMARY KEY

-- Составной индекс (2-3 поля)

    -- Когда постоянно ищете по связке полей
    -- Например: фамилия + имя
    -- Не более 2-3 полей, иначе теряется эффективность


-- Назначение и принципы работы
-- Виды триггеров (BEFORE, AFTER)
-- События (INSERT, UPDATE, DELETE)
-- Область применения
-- Практика с нашей БД студентов

-- Безопасное добавление студента и его документов
-- Контроль целостности при переводе между группами
-- Автоматизация создания студ. билетов
-- Ведение истории изменений
-- Обработка ошибок

-- Откат транзакций
-- Проверка условий в триггерах
-- Логирование проблем
-- Восстановление данных


-- DDL - Таблицы с которыми работает

-- CREATE TABLE Groups (
--     group_id   INTEGER PRIMARY KEY AUTOINCREMENT,
--     group_name TEXT    NOT NULL
--                        UNIQUE
-- );

-- CREATE TABLE GroupsTeachers (
--     group_id   INTEGER NOT NULL,
--     teacher_id INTEGER NOT NULL,
--     FOREIGN KEY (
--         group_id
--     )
--     REFERENCES Groups (group_id),
--     FOREIGN KEY (
--         teacher_id
--     )
--     REFERENCES Teachers (teacher_id) 
-- );
-- CREATE TABLE StudentCards (
--     card_id    INTEGER PRIMARY KEY AUTOINCREMENT,
--     student_id INTEGER NOT NULL
--                        UNIQUE,
--     FOREIGN KEY (
--         student_id
--     )
--     REFERENCES Students (student_id) 
-- );
-- CREATE TABLE Students (
--     student_id  INTEGER PRIMARY KEY AUTOINCREMENT,
--     first_name  TEXT    NOT NULL,
--     middle_name TEXT,
--     last_name   TEXT    NOT NULL,
--     age         INTEGER,
--     group_id    INTEGER,
--     FOREIGN KEY (
--         group_id
--     )
--     REFERENCES Groups (group_id) 
-- );
-- CREATE TABLE Teachers (
--     teacher_id  INTEGER PRIMARY KEY AUTOINCREMENT,
--     first_name  TEXT    NOT NULL,
--     middle_name TEXT,
--     last_name   TEXT    NOT NULL
-- );

-- Как открыть транзакцию?

BEGIN TRANSACTION;

-- Добавим студента
INSERT INTO Students (first_name, last_name)
VALUES ('Николай', 'Басков');

-- Мы можем увидеть его
SELECT * FROM Students;

-- Но если что-то пошло не так, откатим изменения
-- ROLLBACK;

-- Добавим его в группу python412
UPDATE Students
SET group_id = (SELECT group_id FROM Groups WHERE group_name = 'python412')
WHERE student_id = (
    SELECT max(student_id)
    FROM Students
    );


-- Посмотрим на результат
SELECT * FROM Students;

-- Выдадим студенческий билет
INSERT INTO StudentCards (student_id)
VALUES (
    (SELECT max(student_id)
     FROM Students)
);

-- Если всё хорошо, зафиксируем изменения
COMMIT;

--TODO Попробуем сделать транзакцию и следующие операции
-- Создать студента (только имя и фамилия)
-- Назначить его в группу
-- Создать студенческий билет
-- Сделать коммит


-- В SQLite есть два основных случая:

-- При синтаксической ошибке или нарушении ограничений (например, UNIQUE или NOT NULL) транзакция автоматически переходит в состояние "failed" (сбой). После этого любые дальнейшие операции в этой транзакции (кроме ROLLBACK) будут игнорироваться! SQLite не даст тебе сделать COMMIT сломанной транзакции.

-- Если произойдёт системная ошибка (например, диск переполнился, отказ файловой системы), то транзакция также перейдет в состояние сбоя, но SQLite может даже автоматически сделать ROLLBACK в некоторых случаях.

-- Попробуем сделать ошибку внутри транзакции

-- Включить проверку целостности ключей
PRAGMA foreign_keys = ON;


BEGIN TRANSACTION;



-- Это выполнится успешно
INSERT INTO Students (first_name, last_name, group_id)
VALUES ('Сергей', 'Безруков', 1);

-- А тут ошибка! Нет такой группы с ID 999!
INSERT INTO Students (first_name, last_name, group_id)
VALUES ('Филипп', 'Киркоров', 999);


-- Этот INSERT уже не выполнится, потому что транзакция в состоянии сбоя
INSERT INTO Students (first_name, last_name, group_id)
VALUES ('Алла', 'Пугачёва', 1);


COMMIT;
-- ROLLBACK;

SELECT * FROM Students;

------------------------------------------
-- 1. Добавляю в таблицу со студентами email и телефон

-- Можно так, но лучше полную версию команды BEGIN TRANSACTION;
BEGIN;

ALTER TABLE Students
ADD COLUMN email TEXT default Null;

-- Для Django есть смысл указать дефолт, а SQLITE пофиг. Запросы одинаковы
ALTER TABLE Students
ADD COLUMN phone TEXT;


SELECT * FROM Students;
-- ROLLBACK;
COMMIT;

-- 2. Сделаем одиночными индексами поля email и phone, а так же индекс из ФИО составной
BEGIN TRANSACTION;

CREATE INDEX idx_email ON Students(email);
CREATE INDEX idx_phone ON Students(phone);
CREATE INDEX idx_fio ON Students(first_name, middle_name, last_name);

-- Внешний ключ на группы тоже индекс!
CREATE INDEX idx_group_id ON Students(group_id);

COMMIT;

--------------TRIEGGERS-------------------
