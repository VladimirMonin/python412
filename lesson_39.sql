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
    date_of_issue TEXT DEFAULT CURRENT_DATE,
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

    -- Требование уникальности пары ID
   -- UNIQUE(group_id, teacher_id)

   -- Вариант 2 - составной первичный ключ
    PRIMARY KEY(group_id, teacher_id)
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

-- 1. Получим название групп
SELECT * FROM Groups;

-- 2. Получим всех студентов python412 JOIN
SELECT s.first_name, s.middle_name, s.last_name, s.age, g.group_name
FROM Students s
JOIN Groups g ON s.group_id = g.group_id
WHERE g.group_name = 'python412';

-- 3. Соберем всех преподов
SELECT * FROM Teachers;

-- 3.1 Добавляю препода 1 в группу 2
INSERT INTO GroupsTeachers(group_id, teacher_id)
VALUES(2, 1);

-- 4. Я хочу взять Препода с фамилией Киркоров и проверить в каких ID группах он преподает. Таблица преподов левая. Таблица связей M2M правая

SELECT t.teacher_id, t.first_name, t.middle_name, t.last_name, gt.group_id
FROM Teachers t
LEFT JOIN GroupsTeachers gt ON t.teacher_id = gt.teacher_id
WHERE t.last_name = 'Киркоров';


-- Добавим сюда JOIN групп
SELECT t.teacher_id, t.first_name, t.middle_name, t.last_name, gt.group_id, g.group_name
FROM Teachers t
LEFT JOIN GroupsTeachers gt ON t.teacher_id = gt.teacher_id
LEFT JOIN Groups g ON gt.group_id = g.group_id
WHERE t.last_name = 'Киркоров';

-- CONCAN - объединение строк, выведем группы через запятую
SELECT t.first_name, t.last_name, GROUP_CONCAT(g.group_name, ', '), COUNT(g.group_name)
FROM Teachers t
LEFT JOIN GroupsTeachers gt ON t.teacher_id = gt.teacher_id
LEFT JOIN Groups g ON gt.group_id = g.group_id
GROUP BY t.teacher_id;


-- 5. Получим всех студентов преподавателя с фамилией Киркоров
SELECT g.group_name AS "Group", s.first_name AS Student_name, s.last_name AS Student_last_name
FROM Teachers AS t
JOIN GroupsTeachers AS gt ON t.teacher_id = gt.teacher_id
JOIN Groups AS g ON gt.group_id = g.group_id
JOIN Students AS s ON g.group_id = s.group_id
WHERE t.last_name = 'Киркоров';


-- 6. Выборка по всем преподам. Полсчитаем количество студентов и количество групп
SELECT t.first_name, t.last_name, COUNT(s.student_id) AS students_count, COUNT(g.group_id) AS groups_count
FROM Teachers t
JOIN GroupsTeachers gt ON t.teacher_id = gt.teacher_id
JOIN Groups g ON gt.group_id = g.group_id
JOIN Students s ON g.group_id = s.group_id
GROUP BY t.teacher_id;


SELECT t.first_name, t.last_name, s.first_name AS student_name, s.group_id, g.group_name
FROM Teachers t
JOIN GroupsTeachers gt ON t.teacher_id = gt.teacher_id
JOIN Groups g ON gt.group_id = g.group_id
JOIN Students s ON g.group_id = s.group_id
