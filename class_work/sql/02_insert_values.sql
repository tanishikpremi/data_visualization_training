-- ============================================================
-- CLASS WORK | SQL - Inserting Data (DML)
-- Topic: INSERT INTO, Single & Multiple Rows, INSERT SELECT
-- ============================================================

-- Setup: recreate tables first
CREATE TABLE IF NOT EXISTS Students (
    student_id    INT          PRIMARY KEY,
    first_name    VARCHAR(50)  NOT NULL,
    last_name     VARCHAR(50)  NOT NULL,
    email         VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    enrollment_date DATE       DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS Courses (
    course_id   INT          PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits     INT,
    instructor  VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Enrollments (
    enrollment_id INT  PRIMARY KEY,
    student_id    INT,
    course_id     INT,
    grade         CHAR(2)
);

-- ─────────────────────────────────────────────
-- Q1. Insert a single row into Students.
INSERT INTO Students (student_id, first_name, last_name, email, date_of_birth)
VALUES (1, 'Alice', 'Johnson', 'alice@example.com', '2002-04-15');

-- Q2. Insert multiple rows at once.
INSERT INTO Students (student_id, first_name, last_name, email, date_of_birth)
VALUES
    (2, 'Bob',     'Smith',   'bob@example.com',     '2001-09-22'),
    (3, 'Charlie', 'Brown',   'charlie@example.com', '2003-01-10'),
    (4, 'Diana',   'Prince',  'diana@example.com',   '2002-07-30'),
    (5, 'Ethan',   'Hunt',    'ethan@example.com',   '2000-12-05');

-- Q3. Insert courses.
INSERT INTO Courses (course_id, course_name, credits, instructor)
VALUES
    (101, 'Data Structures',      4, 'Dr. Kumar'),
    (102, 'Database Management',  3, 'Prof. Shah'),
    (103, 'Python Programming',   3, 'Dr. Mehta'),
    (104, 'Machine Learning',     4, 'Prof. Rao');

-- Q4. Insert enrollment records.
INSERT INTO Enrollments VALUES (1001, 1, 101, 'A');
INSERT INTO Enrollments VALUES (1002, 1, 103, 'B');
INSERT INTO Enrollments VALUES (1003, 2, 102, 'A');
INSERT INTO Enrollments VALUES (1004, 3, 101, 'B');
INSERT INTO Enrollments VALUES (1005, 4, 104, 'A');
INSERT INTO Enrollments VALUES (1006, 5, 103, 'C');

-- Q5. Insert a row with only required fields (rest take defaults).
INSERT INTO Students (student_id, first_name, last_name)
VALUES (6, 'Frank', 'Castle');

-- Q6. Insert and immediately verify.
INSERT INTO Courses (course_id, course_name, credits, instructor)
VALUES (105, 'Statistics', 3, 'Dr. Iyer');
SELECT * FROM Courses WHERE course_id = 105;

-- Q7. Insert using SELECT from another table (copy pattern).
-- Example: Copy students enrolled in course 101 to an archive table.
CREATE TABLE IF NOT EXISTS DS_Students AS
SELECT s.student_id, s.first_name, s.last_name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.course_id = 101;

SELECT * FROM DS_Students;
