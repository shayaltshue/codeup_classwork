-- 1. Using the example from the lesson, re-create the employees_with_departments table.
CREATE TEMPORARY TABLE employees_with_departments AS
SELECT emp_no, first_name, last_name, dept_no, dept_name
FROM employees.employees
JOIN employees.dept_emp USING(emp_no)
JOIN employees.departments USING(dept_no)
LIMIT 100;

-- 1a. Add a column named full_name to this table. It should be a VARCHAR whose length is the sum of the lengths of the first name and last name columns
ALTER TABLE employees_with_departments ADD full_name VARCHAR (30);

-- 1b. Update the table so that full name column contains the correct data
UPDATE employees_with_departments
SET full_name = CONCAT(first_name, ' ', last_name);

-- c. Remove the first_name and last_name columns from the table.
ALTER TABLE employees_with_departments
DROP first_name, DROP last_name;

-- 1d. What is another way you could have ended up with this same table?
CREATE TEMPORARY TABLE alternate_employees_with_departments AS
SELECT emp_no, dept_no, dept_name, CONCAT(first_name, ' ', last_name)
FROM employees.employees
JOIN employees.dept_emp USING(emp_no)
JOIN employees.departments USING(dept_no)
LIMIT 100;

-- 2. Create a temporary table based on the payment table from the sakila database.
-- Write the SQL necessary to transform the amount column such that
-- it is stored as an integer representing the number of cents of the payment.
-- For example, 1.99 should become 199.
DROP TABLE IF EXISTS avg_dept_salary;

CREATE TEMPORARY TABLE avg_dept_salary AS	
SELECT 
	dept_name, 
	AVG(salary) as average_salary
FROM employees.departments d
JOIN employees.dept_emp de USING(dept_no)
JOIN employees.salaries s USING(emp_no)
WHERE de.to_date > NOW()
	AND s.to_date > NOW()
GROUP BY d.dept_name;

SELECT * FROM avg_dept_salary;

ALTER TABLE avg_dept_salary
ADD mean_avg_all_salaries FLOAT(30, 8);

UPDATE avg_dept_salary
SET mean_avg_all_salaries = (SELECT AVG(salary) FROM employees.salaries WHERE to_date > NOW());

ALTER TABLE avg_dept_salary
ADD stan_dev FLOAT(30, 8);

UPDATE avg_dept_salary
SET stan_dev = (SELECT STD(salary) FROM employees.salaries WHERE to_date > NOW());

ALTER TABLE avg_dept_salary
ADD z_score FLOAT(30, 8);

UPDATE avg_dept_salary
SET z_score = (average_salary - mean_avg_all_salaries) / stan_dev;

SELECT dept_name, z_score FROM avg_dept_salary;


-- 3b. In terms of salary, what is the best department to work for? The worst?
SELECT dept_name, z_score FROM avg_dept_salary ORDER BY z_score DESC LIMIT 1; -- Returns best department
SELECT dept_name, z_score FROM avg_dept_salary ORDER BY z_score LIMIT 1; -- Returns worst department