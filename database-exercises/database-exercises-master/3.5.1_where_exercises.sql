USE employees;

SELECT * from employees;

-- Find all employees with first names 'Irena', 'Vidya', or 'Maya' and who's gender is male — 441
SELECT * FROM employees
WHERE 	
	gender = 'M' AND
		(first_name = 'Irena' OR
		first_name = 'Vidya' OR
		first_name = 'Maya');

-- Find all employees whose last name starts or ends with 'E' — 30,723 rows.
SELECT * 
FROM employees
WHERE last_name LIKE 'E%' OR last_name LIKE '%E';

-- Duplicate the previous query and update it to find all employees whose last name starts and ends with 'E' — 899 rows.
SELECT * 
FROM employees
WHERE last_name LIKE 'E%E';

-- Find all employees hired in the 90s and born on Christmas — 362 rows.
SELECT * 
FROM employees
WHERE 	
	YEAR(hire_date) BETWEEN 1990 AND 1999 AND
		birth_date LIKE '%12-25';

-- Find all employees with a 'q' in their last name but not 'qu' — 547 rows.
SELECT * 
FROM employees
WHERE last_name LIKE '%q%' AND last_name NOT LIKE '%qu%';
