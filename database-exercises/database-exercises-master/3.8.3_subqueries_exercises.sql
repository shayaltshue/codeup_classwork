-- 1. Find all the employees with the same hire date as employee 101010 using a sub-query. (69 Rows)
SELECT * AS employees_with_same_hire_date_as_101010
FROM employees
WHERE hire_date IN 
    (SELECT hire_date
    FROM employees
    WHERE emp_no = 101010);

-- 2. Find all the titles held by all employees with the first name Aamod.
SELECT DISTINCT title
FROM titles
WHERE emp_no IN 
    (SELECT emp_no
    FROM employees
    WHERE first_name = 'Aamod');

-- 3. How many people in the employees table are no longer working for the company?
SELECT COUNT(*) AS count_of_former_employees
FROM employees
WHERE emp_no NOT IN
    (SELECT emp_no
    FROM salaries
    WHERE to_date > NOW());

-- 4. Find all the current department managers that are female.
SELECT first_name, last_name
FROM employees
WHERE gender = 'F' 
    AND emp_no IN
        (SELECT emp_no
        FROM dept_manager
        WHERE to_date > NOW()
        )

-- 5. Find all the employees that currently have a higher than average salary.
    -- 154543 rows in total. Here is what the first 5 rows will look like:
SELECT
	first_name,
	last_name,
	salary
FROM employees
JOIN salaries USING(emp_no)
WHERE salary > (SELECT AVG(salary)
FROM salaries)
	AND salaries.to_date > NOW();

-- 6. How many current salaries are within 1 standard deviation of the highest salary? '
-- (Hint: you can use a built in function to calculate the standard deviation.) 
-- What percentage of all salaries is this?
SELECT (SELECT COUNT(*)
FROM salaries
WHERE salary > 
	(SELECT MAX(salary) - STD(salary) AS result
	FROM salaries
	)
	AND to_date > NOW()) / (SELECT COUNT(*) FROM salaries WHERE to_date > NOW())