--- SQLite создание таблиц

-- Таблица Студенты
CREATE TABLE IF NOT EXISTS Students(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    age INTEGER,
    group_id INTEGER,
    
    FOREIGN KEY (group_id) REFERENCES Groups(group_id)
);

-- Таблица Группы
CREATE TABLE IF NOT EXISTS Groups(
    group_id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT NOT NULL UNIQUE
);

-- Студ. билеты (один к одному - одному студенту соответствует один билет)
CREATE TABLE IF NOT EXISTS StudentCards(
    card_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Преподы
CREATE TABLE IF NOT EXISTS Teachers(
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL
);

-- Сводная таблица многие-ко многим
CREATE TABLE IF NOT EXISTS GroupsTeachers(
    group_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES Groups(group_id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);

-- ТРИ ОСНОВНЫХ ТИПА СВЯЗЕЙ В SQL
-- Один к одному
-- Один ко многим (со стороны одного)
-- Многие ко многим

-- Создадим 2 группы в одном запросе
INSERT INTO Groups(group_name) 
VALUES('python412'), ('javascript412');

-- Создадим 4 студента в одну группу через подзапрос добудем group_id python412

INSERT INTO Students(first_name, middle_name, last_name, age, group_id)
VALUES('Иван', 'Петрович', 'Бунько', 25, (SELECT group_id FROM Groups WHERE group_name = 'python412')),
      ('Владимир', 'Алексндрович', 'Монин', 25, (SELECT group_id FROM Groups WHERE group_name = 'python412')),
      ('Екатерина', 'Александровна', 'Голосняк', 22, (SELECT group_id FROM Groups WHERE group_name = 'python412')),
      ('Григорий', 'Сергеевич', 'Калинин', 23, (SELECT group_id FROM Groups WHERE group_name = 'python412'));


-- Альтернативный запрос
-- INSERT INTO Students(first_name, middle_name, last_name, age, group_id)
-- SELECT 
--     t.first_name, t.middle_name, t.last_name, t.age, g.group_id
-- FROM 
--     (VALUES
--         ('Иван', 'Петрович', 'Бунько', 25),
--         ('Владимир', 'Алексндрович', 'Монин', 25),
--         ('Екатерина', 'Александровна', 'Голосняк', 22),
--         ('Григорий', 'Сергеевич', 'Калинин', 23)
--     ) AS t(first_name, middle_name, last_name, age)
-- CROSS JOIN 
--     (SELECT group_id FROM Groups WHERE group_name = 'python412') AS g;


-- Добудем все группы на экран
SELECT * FROM Groups;


-- Включение проверки целостности базы данных
PRAGMA foreign_keys = ON;


-- Создадим еще 4 студентов в другую группу с ID 2
INSERT INTO Students(first_name, middle_name, last_name, age, group_id)
VALUES('Андрей', 'Сергеевич', 'Козлов', 25, 2),
      ('Алексей', 'Николевич', 'Петров', 25, 2),
      ('Анастасия', 'Петровна', 'Фёдорова', 22, 2),
      ('Анна', 'Сергеевна', 'Беляева', 22, 2);

-- Всем студентам с ID 3 назначим 2
UPDATE Students SET group_id = 25 WHERE group_id = 2;
-- SQLITE_CONSTRAINT: FOREIGN KEY constraint failed

-- Студ. биленты
INSERT INTO StudentCards(student_id)
VALUES(1), (2), (3), (4), (5), (6), (7), (8);

-- Альтернативный
INSERT INTO StudentCards(student_id)
SELECT student_id
FROM Students;

-- Создадим 4 преподавателей
INSERT INTO Teachers(first_name, middle_name, last_name)
VALUES('Филлип', 'Бедросович', 'Киркоров'),
      ('Брюс', 'Петрович', 'Уиллис'),
      ('Сергей', 'Сергеевич', 'Сергеев'),
      ('Алексей', 'Алексеевич', 'Алексеев');


-- Создадим связи многие ко многим
INSERT INTO GroupsTeachers(group_id, teacher_id)
VALUES(1, 1), (1, 2), (2, 3), (2, 4);


---------ВЫБОРКА ДАННЫХ----------------