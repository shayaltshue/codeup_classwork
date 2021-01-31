USE employees;

-- Update your queries for employees whose names start and end with 'E'. 
-- Use concat() to combine their first and last name together as a single column named full_name.
SELECT 
	CONCAT(first_name,' ', last_name) AS full_name
FROM employees
WHERE last_name LIKE 'E%' AND last_name LIKE '%E'
ORDER BY emp_no;

-- Convert the names produced in your last query to all uppercase.
SELECT 
	UPPER(CONCAT(first_name,' ', last_name)) AS full_name
FROM employees
WHERE last_name LIKE 'E%' AND last_name LIKE '%E'
ORDER BY emp_no;

-- For your query of employees born on Christmas and hired in the 90s, 
-- use datediff() to find how many days they have been working at the company 
-- (Hint: You will also need to use NOW() or CURDATE())
SELECT 
	*,
	datediff(NOW(), hire_date) AS days_worked_at_company
FROM employees
WHERE 	YEAR(hire_date) BETWEEN 1990 AND 1999 AND
		birth_date LIKE '%12-25'
ORDER BY birth_date ASC, hire_date DESC;

-- Find the smallest and largest salary from the salaries table.
SELECT
	MIN(salary) AS minimum_salary,
	MAX(salary) AS maximum_salary
FROM salaries;

-- Use your knowledge of built in SQL functions to generate a username for all of the employees.
-- A username should be all lowercase, and 
-- consist of the first character of the employees first name,
-- the first 4 characters of the employees last name,
-- an underscore, 
-- the month the employee was born,
-- and the last two digits of the year that they were born. 
SELECT 
	LOWER(
		CONCAT(
			LEFT(first_name, 1),
			LEFT(last_name, 4),
			'_',
			LPAD(
				MONTH(birth_date), 2, '0'),
			RIGHT(YEAR(birth_date), 2)
		)
	), 
	first_name,
	last_name,
	birth_date
FROM employees;



-- **BONUS ROUND**

-- Find the number of years each employee has been with the company,
-- not just the number of days. *Bonus* do this without the DATEDIFF function (hint: YEAR)
SELECT 
	YEAR(NOW()) - YEAR(hire_date)
FROM employees;

-- Find out how old each employee was when they were hired.
SELECT
	hire_date,
	birth_date,
	YEAR(hire_date) - YEAR(birth_date) AS age_at_hire
FROM employees;

-- Find the most recent date in the dataset. What does this tell you? 
-- Does this explain the distribution of employee ages?
SELECT
	MAX(hire_date)
FROM employees;
-- Answer, latest hiring was 20 years ago on 2000-01-28. No clue if it explains the age distribution