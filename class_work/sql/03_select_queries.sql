-- ============================================================
-- CLASS WORK | SQL - SELECT Queries (DQL)
-- Topic: WHERE, ORDER BY, LIMIT, DISTINCT, LIKE, BETWEEN
-- ============================================================

-- Q1. Select all records from Students.
SELECT * FROM Students;

-- Q2. Select only specific columns.
SELECT first_name, last_name, email FROM Students;

-- Q3. Filter students born after 2001.
SELECT * FROM Students
WHERE date_of_birth > '2001-12-31';

-- Q4. Use AND / OR conditions.
SELECT * FROM Students
WHERE date_of_birth > '2001-01-01' AND last_name LIKE 'S%';

-- Q5. Get distinct departments from Employees.
SELECT DISTINCT department FROM Employees;

-- Q6. Order students by last name alphabetically.
SELECT * FROM Students
ORDER BY last_name ASC;

-- Q7. Get top 3 highest salary employees.
SELECT full_name, salary FROM Employees
ORDER BY salary DESC
LIMIT 3;

-- Q8. Use BETWEEN for salary range.
SELECT full_name, salary FROM Employees
WHERE salary BETWEEN 50000 AND 75000;

-- Q9. Use LIKE for pattern matching.
-- All students whose email ends with @example.com
SELECT * FROM Students
WHERE email LIKE '%@example.com';

-- Q10. Use IN to filter specific departments.
SELECT full_name, department FROM Employees
WHERE department IN ('IT', 'Finance', 'HR');

-- Q11. Count total students.
SELECT COUNT(*) AS total_students FROM Students;

-- Q12. Get average, min, max salary by department.
SELECT
    department,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary)           AS min_salary,
    MAX(salary)           AS max_salary
FROM Employees
GROUP BY department
ORDER BY avg_salary DESC;
