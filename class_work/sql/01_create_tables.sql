-- ============================================================
-- CLASS WORK | SQL - Table Creation (DDL)
-- Topic: CREATE TABLE, Data Types, Constraints, PRIMARY KEY
-- ============================================================

-- Q1. Create a simple Students table.
CREATE TABLE Students (
    student_id   INT          PRIMARY KEY,
    first_name   VARCHAR(50)  NOT NULL,
    last_name    VARCHAR(50)  NOT NULL,
    email        VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    enrollment_date DATE       DEFAULT CURRENT_DATE
);

-- Q2. Create a Courses table.
CREATE TABLE Courses (
    course_id   INT         PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits     INT          CHECK (credits BETWEEN 1 AND 6),
    instructor  VARCHAR(100)
);

-- Q3. Create an Enrollments table with a FOREIGN KEY (junction table).
CREATE TABLE Enrollments (
    enrollment_id INT  PRIMARY KEY,
    student_id    INT  NOT NULL,
    course_id     INT  NOT NULL,
    grade         CHAR(2),
    enrolled_on   DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id)  REFERENCES Courses(course_id)
);

-- Q4. Create an Employees table with multiple constraints.
CREATE TABLE Employees (
    emp_id     INT          PRIMARY KEY AUTO_INCREMENT,
    full_name  VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary     DECIMAL(10,2) CHECK (salary > 0),
    hire_date  DATE,
    is_active  BOOLEAN      DEFAULT TRUE
);

-- Q5. Create a Products table.
CREATE TABLE Products (
    product_id   INT          PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    category     VARCHAR(50),
    price        DECIMAL(8,2) NOT NULL,
    stock_qty    INT          DEFAULT 0,
    created_at   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
);

-- Q6. Alter table — add a new column.
ALTER TABLE Students ADD COLUMN phone VARCHAR(15);

-- Q7. Rename a column (MySQL syntax).
ALTER TABLE Students RENAME COLUMN phone TO contact_number;

-- Q8. Drop a column.
ALTER TABLE Students DROP COLUMN contact_number;

-- Q9. Add an index on a frequently searched column.
CREATE INDEX idx_employee_dept ON Employees(department);

-- Q10. Drop a table safely.
DROP TABLE IF EXISTS Enrollments;
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
