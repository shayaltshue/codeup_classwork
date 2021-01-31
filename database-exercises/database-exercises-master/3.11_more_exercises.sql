-- 1. How much do the current managers of each department get paid, relative to the average salary for the department? 
-- Is there any department where the department manager gets paid less than the average salary?
DROP TABLE IF EXISTS current_managers;

-- Create a temporary table to hold our current managers
CREATE TEMPORARY TABLE current_managers AS
    SELECT
        dm.emp_no,
        CONCAT(first_name, ' ', last_name) as `manager_name`,
        d.dept_name,
        salary    
    FROM employees.dept_manager dm
    JOIN employees.salaries s USING(emp_no)
    JOIN employees.employees e USING(emp_no)
    JOIN employees.departments d USING(dept_no)
    WHERE dm.to_date > NOW()
    	AND s.to_date > NOW();

DROP TABLE IF EXISTS avg_dept_sal;

-- Create a temporary table to calculate the average salary across each department
CREATE TEMPORARY TABLE avg_dept_sal AS
	SELECT 
		dept_name,
		AVG(salary) as avg_salary_of_dept
	FROM employees.salaries s
	JOIN employees.dept_emp USING(emp_no)
	JOIN employees.departments d USING(dept_no)
	GROUP BY dept_name;
	
SELECT * FROM avg_dept_sal;

SELECT
    dept_name,
    manager_name,
    salary,
    avg_salary_of_dept
FROM current_managers
JOIN avg_dept_sal USING(dept_name)
GROUP BY dept_name;

-- Answer: Yes, the manager of Customer Service is making ~$25 less than that department's average!


-- 2.  What languages are spoken in Santa Monica?
USE world;

SELECT 
    name,
    population,
    language,
    percentage
FROM city c
JOIN countrylanguage cl USING(CountryCode)
WHERE name = 'Santa Monica'
ORDER BY percentage DESC;

-- 3. How many different countries are in each region?
USE world;

SELECT
    region,
    COUNT(DISTINCT name) as num_countries
FROM country
GROUP BY region
ORDER BY num_countries;

-- 4. What is the population for each region?
SELECT region,
	SUM(population) as total_population
FROM country
GROUP BY region
ORDER BY total_population DESC;

-- 5. What is the population for each continent?
SELECT continent,
	SUM(population) as total_population
FROM country
GROUP BY continent
ORDER BY total_population DESC;

-- 6. What is the average life expectancy globally?
SELECT AVG(LifeExpectancy)
FROM country;

-- 7. What is the average life expectancy for each region, each continent? Sort the results from shortest to longest
SELECT continent,
	AVG(LifeExpectancy)
FROM country
GROUP BY continent
ORDER BY AVG(LifeExpectancy);

SELECT region,
	AVG(LifeExpectancy)
FROM country
GROUP BY region
ORDER BY AVG(LifeExpectancy);

-- World db BONUS
SELECT
    Name,
    LocalName
FROM (
    SELECT
		name,
		localname,
        CASE
            WHEN country.name != country.LocalName
            THEN 1
            ELSE 0
        END as has_different_local_name
    FROM country
    ) AS a
WHERE has_different_local_name = 1;

------------ SAKILA DATEBASE ------------------
USE sakila;

-- 1. Display the first and last names in all lowercase of all the actors.
SELECT 
    LOWER(CONCAT(first_name, ' ', last_name)) AS actor_name 
FROM actor;

-- 2. You need to find the 
    --ID number, first name, and last name of an actor, 
    --of whom you know only the first name, "Joe." What is one query would you could use to obtain this information?
SELECT
    actor_id,
    first_name,
    last_name
FROM actor
WHERE first_name = "joe";

-- 3. Find all actors whose last name contain the letters "gen":
SELECT *
FROM actor
WHERE last_name LIKE '%gen%';

-- 4. Find all actors whose last names contain the letters "li". This time, 
    -- order the rows by last name and first name, in that order.
SELECT *
FROM actor
WHERE last_name LIKE '%li%'
ORDER BY last_name, first_name;

-- 5. Using IN, display the 
    --country_id and country columns for the following 
    -- countries: Afghanistan, Bangladesh, and China:
SELECT 
    country_id,
    country
FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 6. List the last names of all the actors, as well as how many actors have that last name.
SELECT 
    last_name,
    COUNT(*)
FROM actor
GROUP BY last_name;

-- 7. List last names of actors and the number of actors who have that last name, 
    -- but only for names that are shared by at least two actors
SELECT
    last_name,
    num_of_actors
FROM (
    SELECT
    last_name,
    COUNT(*) as num_of_actors
    FROM actor
    GROUP BY last_name
    ) a
WHERE num_of_actors > 1;

-- 8. You cannot locate the schema of the address table. Which query would you use to re-create it?
SHOW CREATE TABLE address;

-- 9. Use JOIN to display the first and last names, as well as the address, of each staff member.
SELECT
    first_name AS emp_first_name,
    last_name AS emp_last_name,
    address AS store_address
FROM staff
JOIN address USING (address_id);

-- 10. Use JOIN to display the total amount rung up by each staff member in August of 2005.
SELECT 
    CONCAT(first_name, ' ', last_name) as staff_member,
    SUM(amount) AS sales_in_august
FROM staff
JOIN payment USING(staff_id)
WHERE MONTH(payment_date) = 08
GROUP BY staff_id;

-- 11. List each film and the number of actors who are listed for that film.
SELECT
    title,
    COUNT(actor_id)
FROM film
JOIN film_actor USING(film_id)
GROUP BY title;

-- 12. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT
    COUNT(inventory_id)
FROM film
JOIN inventory USING(film_id)
WHERE title = 'Hunchback Impossible';

-- 13. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT
    title
FROM film
WHERE LEFT(title, 1) IN ('Q', 'K')
    AND language_id = (SELECT language_id FROM language WHERE name = 'english');

-- 14. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT
    CONCAT(first_name, ' ', last_name) as actor
    FROM actor
    WHERE actor_id IN (SELECT actor_id
FROM film_actor
WHERE film_id IN (SELECT film_id
FROM film
WHERE title = 'alone trip'));

-- 15. You want to run an email marketing campaign in Canada, 
-- for which you will need the names and email addresses of all Canadian customers.
SELECT email
FROM customer c
JOIN address USING(address_id)
JOIN city USING(city_id)
JOIN country cy using(country_id)
WHERE cy.country = 'Canada';

-- 16. Sales have been lagging among young families, 
-- and you wish to target all family movies for a promotion. Identify all movies categorized as famiy films.
SELECT
    title,
    category.name as genre
FROM film
JOIN film_category USING(film_id)
JOIN category USING(category_id)
WHERE category.name = 'Family';

-- 17. Write a query to display how much business, in dollars, each store brought in.
SELECT 
    store_id,
    SUM(amount) AS total_sales_amount
FROM store
JOIN inventory USING(store_id)
JOIN staff USING(store_id)
JOIN payment USING(staff_id)
GROUP BY store_id;

-- 18. Write a query to display for each store its store ID, city, and country.
SELECT
    store_id,
    city,
    country
FROM store
JOIN address USING(address_id)
JOIN city USING(city_id)
JOIN country USING(country_id)
GROUP BY store_id;

-- 19. List the top five genres in gross revenue in descending order. 
-- (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)
SELECT
    category.name,
    SUM(amount) as gross_rev
FROM payment
JOIN rental USING(rental_id)
JOIN inventory USING(inventory_id)
JOIN film_category USING(film_id)
JOIN category USING(category_id)
GROUP BY category_id
ORDER BY gross_rev DESC
LIMIT 5;

--- 1. SELECT statements
-- a. Select all columns from the actor table.
SELECT * FROM actor;
-- b. Select only the last_name column from the actor table.
SELECT last_name FROM actor;
-- c. Select only the following columns from the film table.
    -- Umm, there's nothing following it so....

--- 2. Distinct Operator
-- a. Select all distinct (different) last names from the actor table.
SELECT DISTINCT last_name FROM actor;
-- b. Select all distinct (different) postal codes from the address table.
SELECT DISTINCT postal_code FROM address;
-- c. Select all distinct (different) ratings from the film table.
SELECT DISTINCT rating FROM film;

-- 3. WHERE clause
-- Select the title, description, rating, movie length columns from the films table that last 3 hours or longer.
SELECT title, description, rating, length FROM film WHERE length > (60 * 3);
-- Select the payment id, amount, and payment date columns from the payments table for payments made on or after 05/27/2005.
SELECT payment_id, amount, payment_date FROM payment WHERE payment_date > 05/27/2005;
-- Select the primary key, amount, and payment date columns from the payment table for payments made on 05/27/2005.
SELECT payment_id, amount, payment_date FROM payment WHERE payment_date = 05/27/2005;
-- Select all columns from the customer table for rows that have a last names beginning with S and a first names ending with N.
SELECT * FROM customer WHERE LEFT(last_name, 1) = 'S' AND LEFT(first_name, 1) = 'N';
-- Select all columns from the customer table for rows where the customer is inactive or has a last name beginning with "M".
SELECT * FROM customer WHERE active = 0 AND LEFT(last_name, 1) = 'N';
-- Select all columns from the category table for rows where the primary key is greater than 4
--  and the name field begins with either C, S or T.
SELECT * FROM category WHERE category_id > 4 AND LEFT(name, 1) IN ('C', 'S', 'T');
-- Select all columns minus the password column from the staff table for rows that contain a password.
SELECT * FROM staff WHERE password = 1;
-- Select all columns minus the password column from the staff table for rows that do not contain a password.


-- 4. IN operator
-- Select the phone and district columns from the address table for addresses in California, England, Taipei, or West Java.
SELECT phone, district FROM address WHERE DISTRICT IN ('California', 'England', 'Taipei', 'West Java');
-- Select the payment id, amount, and payment date columns from the payment table for payments made on 
-- 05/25/2005, 05/27/2005, and 05/29/2005. 
-- (Use the IN operator and the DATE function, instead of the AND operator as in previous exercises.)
SELECT payment_id, amount, payment_date FROM payment WHERE DATE(payment_date) IN (05/25/2005, 05/27/2005, 05/29/2005);

-- Select all columns from the film table for films rated G, PG-13 or NC-17.