-- self learning - GROUP BY, HAVING, aggregate functions
-- revisiting this because i kept mixing up WHERE and HAVING
-- key difference: WHERE filters rows BEFORE grouping, HAVING filters AFTER

-- ── basic GROUP BY ──────────────────────────────

-- how many employees are in each department?
SELECT department, COUNT(*) AS headcount
FROM Employees
GROUP BY department;

-- total salary bill per department
SELECT department, SUM(salary) AS total_salary_bill
FROM Employees
GROUP BY department
ORDER BY total_salary_bill DESC;

-- ── multiple aggregations ───────────────────────

SELECT
    department,
    COUNT(*)                    AS headcount,
    ROUND(AVG(salary), 2)      AS avg_salary,
    MIN(salary)                 AS min_salary,
    MAX(salary)                 AS max_salary,
    SUM(salary)                 AS total_salary
FROM Employees
GROUP BY department;

-- ── HAVING - filter on aggregated values ────────
-- (WHERE can't use aggregate functions - that's why HAVING exists)

-- departments with more than 3 employees
SELECT department, COUNT(*) AS headcount
FROM Employees
GROUP BY department
HAVING COUNT(*) > 3;

-- departments where avg salary is above 65000
SELECT department, ROUND(AVG(salary), 2) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > 65000
ORDER BY avg_salary DESC;

-- ── WHERE + GROUP BY + HAVING together ──────────

-- among ACTIVE employees, which departments have avg salary > 60k?
SELECT department, ROUND(AVG(salary), 2) AS avg_sal
FROM Employees
WHERE is_active = TRUE          -- filters rows first
GROUP BY department
HAVING AVG(salary) > 60000      -- filters groups after
ORDER BY avg_sal DESC;

-- ── GROUP BY multiple columns ───────────────────

-- count students per grade per course
SELECT
    c.course_name,
    e.grade,
    COUNT(*) AS student_count
FROM Enrollments e
JOIN Courses c ON e.course_id = c.course_id
GROUP BY c.course_name, e.grade
ORDER BY c.course_name, e.grade;

-- ── WITH ROLLUP - adds subtotals ────────────────
-- (mysql specific, interesting feature)

SELECT
    COALESCE(department, 'TOTAL') AS department,
    COUNT(*) AS headcount,
    SUM(salary) AS total_salary
FROM Employees
GROUP BY department WITH ROLLUP;

-- MISTAKES I KEPT MAKING:
-- ❌ SELECT department, COUNT(*) FROM Employees WHERE COUNT(*) > 3 → WRONG
-- ✅ SELECT department, COUNT(*) FROM Employees GROUP BY department HAVING COUNT(*) > 3
--
-- ❌ can't SELECT a non-aggregated column that's not in GROUP BY
-- ✅ every column in SELECT must either be in GROUP BY or wrapped in aggregate
