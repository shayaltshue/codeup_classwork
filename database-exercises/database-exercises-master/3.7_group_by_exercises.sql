-- Use DISTINCT to find the unique titles in the titles table. 
SELECT
    UNIQUE title
FROM titles;

-- Find your query for employees whose last names start and end with 'E'. 
SELECT
    last_name
FROM employees
WHERE last_name LIKE 'e%' AND last_name LIKE '%e';


-- Update the query find just the unique last names that start and end with 'E' using GROUP BY.
SELECT  
	last_name
FROM employees
WHERE last_name LIKE 'e%e'
GROUP BY last_name;

-- Update your previous query to now find unique combinations of first and last name
-- where the last name starts and ends with 'E'. You should get 846 rows.
SELECT  
    first_name
	last_name
FROM employees
WHERE last_name LIKE 'e%e'
GROUP BY first_name, last_name;

-- Find the unique last names with a 'q' but not 'qu'.
SELECT
    last_name
FROM employees
WHERE last_name LIKE '%q%' 
    AND last_name NOT LIKE '%qu%'
GROUP BY last_name;

-- Add a COUNT() to your results and use ORDER BY to make it easier to find employees
-- whose unusual name is shared with others.
SELECT
	last_name,
    COUNT(*)
FROM employees
WHERE  last_name LIKE '%q%' 
    AND last_name NOT LIKE '%qu%'
GROUP BY last_name;

-- Update your query for 'Irena', 'Vidya', or 'Maya'.
-- Use COUNT(*) and GROUP BY to find the number of employees for each gender with those names.
SELECT 
	COUNT(*),
	gender
FROM employees
WHERE first_name IN ('Vidya', 'Irena', 'Maya')
GROUP BY gender;

-- Recall the query the generated usernames for the employees from the last lesson. 
-- Are there any duplicate usernames?
SELECT
    LOWER(
        CONCAT(
            LEFT(first_name, 1),
            LEFT(last_name, 4),
            '_',
            LPAD(MONTH(birth_date), 2, '0'),
            RIGHT(YEAR(birth_date), 2)
            )
        )  as user_name,
    COUNT(*)
FROM employees
GROUP BY user_name  
HAVING count(user_name) > 1
ORDER BY COUNT(*);  

