-- self learning - SQL practice
-- topic: subqueries
-- these confused me in class, practicing on my own to understand better

-- ── what is a subquery? ────────────────────────
-- it's just a query inside another query
-- inner query runs first, then the outer query uses that result

-- Q1. find employees who earn more than the average salary
-- (tried doing this without subquery first - couldn't do it in one query)

SELECT full_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
ORDER BY salary DESC;

-- Q2. find the employee with the highest salary
-- (could also use ORDER BY + LIMIT but this is the subquery way)

SELECT full_name, salary
FROM Employees
WHERE salary = (SELECT MAX(salary) FROM Employees);

-- Q3. subquery in FROM clause (inline view / derived table)
-- get departments with avg salary above 60000

SELECT department, avg_sal
FROM (
    SELECT department, ROUND(AVG(salary), 2) AS avg_sal
    FROM Employees
    GROUP BY department
) AS dept_avg
WHERE avg_sal > 60000;

-- Q4. correlated subquery - runs for EACH row of the outer query
-- find employees who earn more than the avg salary IN THEIR department
-- NOTE: this one is slower but very powerful

SELECT e.full_name, e.department, e.salary
FROM Employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department  -- this links to the outer query row
);

-- Q5. EXISTS - check if something exists in another table
-- find customers who have placed at least one order

-- SELECT name FROM Customers c
-- WHERE EXISTS (
--     SELECT 1 FROM Orders o WHERE o.customer_id = c.customer_id
-- );

-- Q6. NOT EXISTS - opposite of above
-- find students not enrolled in any course

SELECT first_name, last_name
FROM Students s
WHERE NOT EXISTS (
    SELECT 1 FROM Enrollments e WHERE e.student_id = s.student_id
);

-- Q7. IN with subquery
-- find all courses that have at least one enrollment

SELECT course_name
FROM Courses
WHERE course_id IN (SELECT DISTINCT course_id FROM Enrollments);

-- Q8. NOT IN - courses with NO enrollments
SELECT course_name
FROM Courses
WHERE course_id NOT IN (SELECT DISTINCT course_id FROM Enrollments);

-- NOTES TO SELF:
-- correlated subquery = slow (runs per row), use JOIN when possible
-- EXISTS is usually faster than IN for large datasets
-- scalar subquery = returns exactly one value (used in WHERE/SELECT)
