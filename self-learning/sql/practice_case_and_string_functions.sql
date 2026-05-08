-- self learning - CASE statements + string/date functions
-- picked this up while going through some interview questions online
-- very useful for creating conditional columns

-- ── CASE WHEN (like if-else in SQL) ───────────

-- categorize employees by salary
SELECT
    full_name,
    salary,
    CASE
        WHEN salary >= 80000 THEN 'Senior'
        WHEN salary >= 60000 THEN 'Mid-Level'
        WHEN salary >= 40000 THEN 'Junior'
        ELSE 'Intern'
    END AS level
FROM Employees;

-- grade conversion from letter to GPA
SELECT
    student_id,
    grade,
    CASE grade
        WHEN 'A'  THEN 4.0
        WHEN 'A-' THEN 3.7
        WHEN 'B'  THEN 3.0
        WHEN 'B-' THEN 2.7
        WHEN 'C'  THEN 2.0
        ELSE 1.0
    END AS gpa
FROM Enrollments;

-- ── CASE in aggregation (conditional count) ────
-- count how many A, B, C grade students per course

SELECT
    course_id,
    COUNT(CASE WHEN grade = 'A' THEN 1 END) AS a_students,
    COUNT(CASE WHEN grade = 'B' THEN 1 END) AS b_students,
    COUNT(CASE WHEN grade = 'C' THEN 1 END) AS c_students
FROM Enrollments
GROUP BY course_id;

-- ── string functions (MySQL) ────────────────────

-- CONCAT, LENGTH, UPPER, LOWER, TRIM
SELECT
    CONCAT(first_name, ' ', last_name)  AS full_name,
    LENGTH(email)                        AS email_length,
    UPPER(first_name)                    AS name_upper,
    SUBSTRING(email, 1, 5)               AS email_preview
FROM Students;

-- extract domain from email
SELECT
    email,
    SUBSTRING_INDEX(email, '@', -1) AS domain
FROM Students;

-- ── date functions ──────────────────────────────

-- current date and time
SELECT NOW(), CURDATE(), CURTIME();

-- extract parts of a date
SELECT
    enrollment_date,
    YEAR(enrollment_date)    AS yr,
    MONTH(enrollment_date)   AS mo,
    DAY(enrollment_date)     AS dy,
    DAYNAME(enrollment_date) AS day_name,
    MONTHNAME(enrollment_date) AS month_name
FROM Students
WHERE enrollment_date IS NOT NULL;

-- difference between two dates
SELECT
    first_name,
    date_of_birth,
    TIMESTAMPDIFF(YEAR, date_of_birth, CURDATE()) AS age
FROM Students;

-- filter records from last 30 days
SELECT * FROM Enrollments
WHERE enrolled_on >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);

-- NOTE: date functions vary between MySQL / PostgreSQL / SQLite
-- MySQL:      CURDATE(), DATE_SUB(), TIMESTAMPDIFF()
-- PostgreSQL: CURRENT_DATE, interval '30 days', AGE()
-- SQLite:     date('now'), julianday()
