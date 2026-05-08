-- ============================================================
-- CLASS WORK | SQL - UPDATE & DELETE (DML)
-- Topic: UPDATE SET, DELETE, TRUNCATE, Safe Deletes
-- ============================================================

-- Q1. Update a student's email.
UPDATE Students
SET email = 'alice.johnson@newmail.com'
WHERE student_id = 1;

-- Q2. Give all IT department employees a 10% salary raise.
UPDATE Employees
SET salary = salary * 1.10
WHERE department = 'IT';

-- Q3. Update multiple columns at once.
UPDATE Employees
SET department = 'Tech', salary = 80000
WHERE emp_id = 5;

-- Q4. Set a default value for NULLs.
UPDATE Students
SET email = CONCAT(first_name, '.', last_name, '@school.edu')
WHERE email IS NULL;

-- Q5. Delete a specific enrollment.
DELETE FROM Enrollments
WHERE enrollment_id = 1006;

-- Q6. Delete all students who have no enrollments.
DELETE FROM Students
WHERE student_id NOT IN (SELECT DISTINCT student_id FROM Enrollments);

-- Q7. Delete employees whose hire date is before 2015.
DELETE FROM Employees
WHERE hire_date < '2015-01-01';

-- Q8. TRUNCATE — delete all rows but keep the table structure.
-- ⚠️ Warning: This cannot be rolled back in most databases.
-- TRUNCATE TABLE DS_Students;

-- Q9. Safe delete with a transaction (rollback if something goes wrong).
START TRANSACTION;
DELETE FROM Enrollments WHERE course_id = 104;
-- ROLLBACK;   -- Uncomment to undo
COMMIT;

-- Q10. Verify updates/deletes.
SELECT * FROM Students;
SELECT * FROM Employees ORDER BY emp_id;
SELECT * FROM Enrollments;
