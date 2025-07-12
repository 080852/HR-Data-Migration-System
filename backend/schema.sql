CREATE TABLE legacy_employees (
    emp_id INT,
    full_name VARCHAR(100),
    dob VARCHAR(20),
    dept_code VARCHAR(10),
    email TEXT,
    salary VARCHAR(20),
    gender CHAR(1)
);

CREATE TABLE modern_employees (
    emp_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    department VARCHAR(50),
    email TEXT,
    salary INT,
    gender VARCHAR(10)
);
