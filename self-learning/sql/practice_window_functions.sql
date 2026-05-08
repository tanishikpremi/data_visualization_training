-- self learning - window functions
-- honestly didn't even know these existed until i saw them in a project
-- they're like GROUP BY but you keep all the rows instead of collapsing them

-- ── ROW_NUMBER ─────────────────────────────────
-- assigns a unique number to each row within a partition

SELECT
    full_name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM Employees;
-- row_num resets to 1 for each new department

-- ── RANK vs DENSE_RANK ──────────────────────────
-- RANK: skips numbers on ties (1, 2, 2, 4)
-- DENSE_RANK: no skipping (1, 2, 2, 3)

SELECT
    full_name,
    salary,
    RANK()       OVER (ORDER BY salary DESC) AS rank_val,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank_val
FROM Employees;

-- ── NTILE ──────────────────────────────────────
-- divides rows into N buckets
-- useful for quartiles, deciles

SELECT
    full_name,
    salary,
    NTILE(4) OVER (ORDER BY salary) AS salary_quartile
FROM Employees;
-- quartile 1 = lowest 25%, quartile 4 = highest 25%

-- ── running totals with SUM OVER ───────────────

SELECT
    full_name,
    hire_date,
    salary,
    SUM(salary) OVER (ORDER BY hire_date) AS running_total
FROM Employees
ORDER BY hire_date;

-- ── LAG and LEAD - comparing with previous/next row ──
-- really useful for month-over-month comparisons

-- (example with a monthly sales table)
-- SELECT
--     month,
--     revenue,
--     LAG(revenue, 1)  OVER (ORDER BY month) AS prev_month_revenue,
--     LEAD(revenue, 1) OVER (ORDER BY month) AS next_month_revenue,
--     revenue - LAG(revenue, 1) OVER (ORDER BY month) AS change
-- FROM monthly_sales;

-- ── practical use: top 3 earners per department ────
-- this is the thing i was trying to do with subqueries before!
-- window functions make it way cleaner

SELECT department, full_name, salary
FROM (
    SELECT
        department,
        full_name,
        salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rnk
    FROM Employees
) ranked
WHERE rnk <= 3;

-- NOTES:
-- OVER()           = apply to whole result set
-- PARTITION BY     = restart window for each group (like GROUP BY but keeps rows)
-- ORDER BY inside  = controls the order within each window
-- ROWS BETWEEN ... = define frame for running calculations
