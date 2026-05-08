-- ============================================================
-- CLASS WORK | SQL - JOIN Queries
-- Topic: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
-- ============================================================

-- ─────────────────────────────────────────────
-- Sample Setup (reuse from previous files)
-- ─────────────────────────────────────────────

-- Q1. INNER JOIN — Students who are enrolled in any course.
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    c.course_name,
    e.grade
FROM Students s
INNER JOIN Enrollments e ON s.student_id = e.student_id
INNER JOIN Courses c     ON e.course_id  = c.course_id;

-- Q2. LEFT JOIN — All students, even those not enrolled.
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
LEFT JOIN Courses c     ON e.course_id  = c.course_id;

-- Q3. Find students who are NOT enrolled in any course.
SELECT s.first_name, s.last_name
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- Q4. Count how many students are in each course.
SELECT
    c.course_name,
    COUNT(e.student_id) AS total_students
FROM Courses c
LEFT JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY total_students DESC;

-- Q5. Self JOIN — Find employees in the same department.
SELECT
    a.full_name AS Employee1,
    b.full_name AS Employee2,
    a.department
FROM Employees a
JOIN Employees b ON a.department = b.department AND a.emp_id < b.emp_id
ORDER BY a.department;

-- Q6. JOIN with aggregation — Average grade per course.
SELECT
    c.course_name,
    AVG(CASE e.grade
        WHEN 'A' THEN 4.0
        WHEN 'B' THEN 3.0
        WHEN 'C' THEN 2.0
        ELSE 1.0 END) AS avg_gpa
FROM Courses c
JOIN Enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Q7. Subquery with JOIN — Students earning above average salary (Employees).
SELECT full_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
ORDER BY salary DESC;
