from sqlalchemy.orm import Session
from app.database import get_app_db, AppSessionLocal, BaseApp, app_engine
from app.models_app import AppUser, Lesson, Example, Question, UserProgress

def seed_content():
    # drop all existing app tables to rebuild cleanly
    BaseApp.metadata.drop_all(bind=app_engine)
    BaseApp.metadata.create_all(bind=app_engine)
    
    db = AppSessionLocal()
    
    # ------------------ Level 1: SELECT & WHERE (20 Questions) ------------------
    l1 = Lesson(level=1, title="Level 1: SELECT & WHERE", content="""
### 🔹 Foundations: SELECT & WHERE

The `SELECT` statement is the heart of SQL. It tells the database which columns you want to see, while `WHERE` filters the rows based on specific conditions.

#### 1. The SELECT Statement
Used to fetch data from a table. You can fetch specific columns or use `*` for everything.
*   **Syntax**: `SELECT name, email FROM users;`
*   **Pro Tip**: In production, avoid `SELECT *`. Only fetch what you need to save bandwidth and memory!

#### 2. The WHERE Clause
Used to filter records. Only rows that fulfill the condition will be returned.
*   **Scenario**: Find customers from a specific city or users above a certain age.
*   **Syntax**: `SELECT * FROM users WHERE age > 25;`

---
**💡 Interview Fact**: `WHERE` filters rows **before** any grouping or aggregation happens.
""")
    db.add(l1)
    db.flush()
    db.add_all([
        Question(lesson_id=l1.id, question_type="guided", question_text="Fetch all users", expected_query="SELECT * FROM users;", hint="SELECT *", solution="SELECT * FROM users;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users from 'India'", expected_query="SELECT * FROM users WHERE country = 'India';", hint="WHERE country = 'India'", solution="SELECT * FROM users WHERE country = 'India';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users older than 40", expected_query="SELECT * FROM users WHERE age > 40;", hint="WHERE age > 40", solution="SELECT * FROM users WHERE age > 40;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="List names and emails only.", expected_query="SELECT name, email FROM users;", hint="SELECT name, email", solution="SELECT name, email FROM users;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find products priced over 500.", expected_query="SELECT * FROM products WHERE price > 500;", hint="price > 500", solution="SELECT * FROM products WHERE price > 500;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find all 'completed' orders.", expected_query="SELECT * FROM orders WHERE status = 'completed';", hint="status = 'completed'", solution="SELECT * FROM orders WHERE status = 'completed';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users from USA younger than 25.", expected_query="SELECT * FROM users WHERE country = 'United States' AND age < 25;", hint="Use AND", solution="SELECT * FROM users WHERE country = 'United States' AND age < 25;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="List all 'Clothing' items.", expected_query="SELECT * FROM products WHERE category = 'Clothing';", hint="category = 'Clothing'", solution="SELECT * FROM products WHERE category = 'Clothing';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find orders with amount > 1000.", expected_query="SELECT * FROM orders WHERE amount > 1000;", hint="amount > 1000", solution="SELECT * FROM orders WHERE amount > 1000;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find payments via 'credit_card'.", expected_query="SELECT * FROM payments WHERE payment_method = 'credit_card';", hint="payment_method = 'credit_card'", solution="SELECT * FROM payments WHERE payment_method = 'credit_card';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users not from India.", expected_query="SELECT * FROM users WHERE country != 'India';", hint="Use !=", solution="SELECT * FROM users WHERE country != 'India';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users exactly age 30.", expected_query="SELECT * FROM users WHERE age = 30;", hint="age = 30", solution="SELECT * FROM users WHERE age = 30;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find products exactly 9.99.", expected_query="SELECT * FROM products WHERE price = 9.99;", hint="price = 9.99", solution="SELECT * FROM products WHERE price = 9.99;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find orders where status is NOT 'cancelled'.", expected_query="SELECT * FROM orders WHERE status != 'cancelled';", hint="status != 'cancelled'", solution="SELECT * FROM orders WHERE status != 'cancelled';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users from Brazil and age > 20.", expected_query="SELECT * FROM users WHERE country = 'Brazil' AND age > 20;", hint="Use AND", solution="SELECT * FROM users WHERE country = 'Brazil' AND age > 20;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="List all payment statuses.", expected_query="SELECT DISTINCT payment_status FROM payments;", hint="Use DISTINCT", solution="SELECT DISTINCT payment_status FROM payments;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find order items with quantity > 3.", expected_query="SELECT * FROM order_items WHERE quantity > 3;", hint="quantity > 3", solution="SELECT * FROM order_items WHERE quantity > 3;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users from Canada.", expected_query="SELECT * FROM users WHERE country = 'Canada';", hint="country = 'Canada'", solution="SELECT * FROM users WHERE country = 'Canada';"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find products with id 10.", expected_query="SELECT * FROM products WHERE id = 10;", hint="id = 10", solution="SELECT * FROM products WHERE id = 10;"),
        Question(lesson_id=l1.id, question_type="challenge", question_text="Find users aged 18.", expected_query="SELECT * FROM users WHERE age = 18;", hint="age = 18", solution="SELECT * FROM users WHERE age = 18;")
    ])

    # ------------------ Level 2: LIKE, IN, BETWEEN (20 Questions) ------------------
    l2 = Lesson(level=2, title="Level 2: LIKE, IN, BETWEEN", content="""
### 🔹 Pattern Matching & Ranges

Level 2 introduces more flexible ways to filter data beyond simple equality (key = value).

#### 1. LIKE (Pattern Matching)
Used to search for a specified pattern in a column.
*   **%**: Represents zero, one, or multiple characters.
*   **_**: Represents a single character.
*   **Example**: `WHERE name LIKE 'A%'` finds all names starting with 'A'.

#### 2. IN (Selection from List)
Allows you to specify multiple values in a `WHERE` clause. It is shorthand for multiple `OR` conditions.
*   **Syntax**: `SELECT * FROM users WHERE country IN ('India', 'USA', 'UK');`

#### 3. BETWEEN (Range Check)
Selects values within a given range (inclusive).
*   **Syntax**: `SELECT * FROM products WHERE price BETWEEN 10 AND 50;`

---
**💡 Pro Tip**: Use `NOT LIKE`, `NOT IN`, and `NOT BETWEEN` to find everything *except* what matches the criteria!
""")
    db.add(l2)
    db.flush()
    db.add_all([
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find names starting with 'A'.", expected_query="SELECT * FROM users WHERE name LIKE 'A%';", hint="LIKE 'A%'", solution="SELECT * FROM users WHERE name LIKE 'A%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find users from India or USA.", expected_query="SELECT * FROM users WHERE country IN ('India', 'United States');", hint="Use IN", solution="SELECT * FROM users WHERE country IN ('India', 'United States');"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find products priced 10 to 50.", expected_query="SELECT * FROM products WHERE price BETWEEN 10 AND 50;", hint="Use BETWEEN", solution="SELECT * FROM products WHERE price BETWEEN 10 AND 50;"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find emails with 'gmail'.", expected_query="SELECT * FROM users WHERE email LIKE '%gmail%';", hint="LIKE '%gmail%'", solution="SELECT * FROM users WHERE email LIKE '%gmail%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find ages in (18, 25, 30).", expected_query="SELECT * FROM users WHERE age IN (18, 25, 30);", hint="Use IN", solution="SELECT * FROM users WHERE age IN (18, 25, 30);"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find names ending with 'n'.", expected_query="SELECT * FROM users WHERE name LIKE '%n';", hint="LIKE '%n'", solution="SELECT * FROM users WHERE name LIKE '%n';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find IDs between 100 and 200.", expected_query="SELECT * FROM users WHERE id BETWEEN 100 AND 200;", hint="BETWEEN 100 AND 200", solution="SELECT * FROM users WHERE id BETWEEN 100 AND 200;"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find categories like 'Elect%'.", expected_query="SELECT * FROM products WHERE category LIKE 'Elect%';", hint="LIKE 'Elect%'", solution="SELECT * FROM products WHERE category LIKE 'Elect%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find amounts between 500 and 1000.", expected_query="SELECT * FROM orders WHERE amount BETWEEN 500 AND 1000;", hint="BETWEEN 500 AND 1000", solution="SELECT * FROM orders WHERE amount BETWEEN 500 AND 1000;"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find countries NOT in ('India', 'Brazil').", expected_query="SELECT * FROM users WHERE country NOT IN ('India', 'Brazil');", hint="NOT IN", solution="SELECT * FROM users WHERE country NOT IN ('India', 'Brazil');"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find products NOT priced 0 to 10.", expected_query="SELECT * FROM products WHERE price NOT BETWEEN 0 AND 10;", hint="NOT BETWEEN", solution="SELECT * FROM products WHERE price NOT BETWEEN 0 AND 10;"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find names with 'y' as second letter.", expected_query="SELECT * FROM users WHERE name LIKE '_y%';", hint="LIKE '_y%'", solution="SELECT * FROM users WHERE name LIKE '_y%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find users from countries starting with 'U'.", expected_query="SELECT * FROM users WHERE country LIKE 'U%';", hint="LIKE 'U%'", solution="SELECT * FROM users WHERE country LIKE 'U%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find categories 'Toys' or 'Home'.", expected_query="SELECT * FROM products WHERE category IN ('Toys', 'Home');", hint="Use IN", solution="SELECT * FROM products WHERE category IN ('Toys', 'Home');"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find products whose name contains 'Pro'.", expected_query="SELECT * FROM products WHERE name LIKE '%Pro%';", hint="LIKE '%Pro%'", solution="SELECT * FROM products WHERE name LIKE '%Pro%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find ages NOT in (18, 20).", expected_query="SELECT * FROM users WHERE age NOT IN (18, 20);", hint="NOT IN", solution="SELECT * FROM users WHERE age NOT IN (18, 20);"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find products with price between 0.99 and 5.99.", expected_query="SELECT * FROM products WHERE price BETWEEN 0.99 AND 5.99;", hint="BETWEEN", solution="SELECT * FROM products WHERE price BETWEEN 0.99 AND 5.99;"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find users whose name starts with 'J' and ends with 'e'.", expected_query="SELECT * FROM users WHERE name LIKE 'J%e';", hint="LIKE 'J%e'", solution="SELECT * FROM users WHERE name LIKE 'J%e';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find categories NOT containing 's'.", expected_query="SELECT DISTINCT category FROM products WHERE category NOT LIKE '%s%';", hint="NOT LIKE '%s%'", solution="SELECT DISTINCT category FROM products WHERE category NOT LIKE '%s%';"),
        Question(lesson_id=l2.id, question_type="challenge", question_text="Find IDs in (1, 3, 5, 7, 9).", expected_query="SELECT * FROM users WHERE id IN (1, 3, 5, 7, 9);", hint="IN (1, 3, 5, 7, 9)", solution="SELECT * FROM users WHERE id IN (1, 3, 5, 7, 9);")
    ])

    # ------------------ Level 3: Sorting & Limiting (20 Questions) ------------------
    l3 = Lesson(level=3, title="Level 3: Sorting & Limiting", content="""
### 🔹 Presentation: ORDER BY & LIMIT

Data is often useless unless it's organized. These commands help you sort and paginate your results.

#### 1. ORDER BY (Sorting)
Used to sort the result-set in ascending (ASC) or descending (DESC) order.
*   **Syntax**: `SELECT * FROM users ORDER BY created_at DESC;`
*   **Multi-Sort**: `ORDER BY country ASC, age DESC;`

#### 2. LIMIT & OFFSET (Pagination)
`LIMIT` specifies the number of records to return. `OFFSET` skips a specific number of records.
*   **Scenario**: Showing "Top 10" products or implementing page 2 of a website.
*   **Syntax**: `SELECT * FROM users LIMIT 10 OFFSET 10;` (Gets the next 10 users).

---
**💡 Interview Tip**: If you don't specify `ORDER BY`, the database does **not** guarantee any specific order!
""")
    db.add(l3)
    db.flush()
    db.add_all([
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 5 oldest users.", expected_query="SELECT * FROM users ORDER BY age DESC LIMIT 5;", hint="ORDER BY age DESC LIMIT 5", solution="SELECT * FROM users ORDER BY age DESC LIMIT 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="10 cheapest products.", expected_query="SELECT * FROM products ORDER BY price ASC LIMIT 10;", hint="ORDER BY price ASC LIMIT 10", solution="SELECT * FROM products ORDER BY price ASC LIMIT 10;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 3 expensive Electronics.", expected_query="SELECT * FROM products WHERE category = 'Electronics' ORDER BY price DESC LIMIT 3;", hint="WHERE ... ORDER BY ... LIMIT ...", solution="SELECT * FROM products WHERE category = 'Electronics' ORDER BY price DESC LIMIT 3;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="All users sorted alphabetically.", expected_query="SELECT * FROM users ORDER BY name ASC;", hint="ORDER BY name ASC", solution="SELECT * FROM users ORDER BY name ASC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 5 highest orders.", expected_query="SELECT * FROM orders ORDER BY amount DESC LIMIT 5;", hint="ORDER BY amount DESC LIMIT 5", solution="SELECT * FROM orders ORDER BY amount DESC LIMIT 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="10 most recent users.", expected_query="SELECT * FROM users ORDER BY created_at DESC LIMIT 10;", hint="ORDER BY created_at DESC LIMIT 10", solution="SELECT * FROM users ORDER BY created_at DESC LIMIT 10;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="3 youngest from Brazil.", expected_query="SELECT * FROM users WHERE country = 'Brazil' ORDER BY age ASC LIMIT 3;", hint="WHERE ... ORDER BY ... LIMIT ...", solution="SELECT * FROM users WHERE country = 'Brazil' ORDER BY age ASC LIMIT 3;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Users by country, then age (oldest).", expected_query="SELECT * FROM users ORDER BY country, age DESC;", hint="ORDER BY country, age DESC", solution="SELECT * FROM users ORDER BY country, age DESC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Products by category, then price DESC.", expected_query="SELECT * FROM products ORDER BY category, price DESC;", hint="ORDER BY category, price DESC", solution="SELECT * FROM products ORDER BY category, price DESC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Pagination: next 5 users after first 5.", expected_query="SELECT * FROM users LIMIT 5 OFFSET 5;", hint="LIMIT 5 OFFSET 5", solution="SELECT * FROM users LIMIT 5 OFFSET 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 1 expensive Toy.", expected_query="SELECT * FROM products WHERE category = 'Toys' ORDER BY price DESC LIMIT 1;", hint="LIMIT 1", solution="SELECT * FROM products WHERE category = 'Toys' ORDER BY price DESC LIMIT 1;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="All categories A-Z.", expected_query="SELECT DISTINCT category FROM products ORDER BY category ASC;", hint="DISTINCT ... ORDER BY", solution="SELECT DISTINCT category FROM products ORDER BY category ASC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 5 pending orders.", expected_query="SELECT * FROM orders WHERE status = 'pending' ORDER BY amount DESC LIMIT 5;", hint="WHERE ... ORDER BY ... LIMIT ...", solution="SELECT * FROM orders WHERE status = 'pending' ORDER BY amount DESC LIMIT 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="10 most expensive products.", expected_query="SELECT * FROM products ORDER BY price DESC LIMIT 10;", hint="ORDER BY price DESC LIMIT 10", solution="SELECT * FROM products ORDER BY price DESC LIMIT 10;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 5 users from Canada by age.", expected_query="SELECT * FROM users WHERE country = 'Canada' ORDER BY age DESC LIMIT 5;", hint="WHERE ... ORDER BY ... LIMIT ...", solution="SELECT * FROM users WHERE country = 'Canada' ORDER BY age DESC LIMIT 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Cheapest 5 orders.", expected_query="SELECT * FROM orders ORDER BY amount ASC LIMIT 5;", hint="ORDER BY amount ASC LIMIT 5", solution="SELECT * FROM orders ORDER BY amount ASC LIMIT 5;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Users by age, then name.", expected_query="SELECT * FROM users ORDER BY age, name;", hint="ORDER BY age, name", solution="SELECT * FROM users ORDER BY age, name;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Sorting users by most recently registered.", expected_query="SELECT * FROM users ORDER BY created_at DESC;", hint="ORDER BY created_at DESC", solution="SELECT * FROM users ORDER BY created_at DESC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Fetch IDs only, sorted highest to lowest.", expected_query="SELECT id FROM users ORDER BY id DESC;", hint="SELECT id ORDER BY id DESC", solution="SELECT id FROM users ORDER BY id DESC;"),
        Question(lesson_id=l3.id, question_type="challenge", question_text="Top 1 highest amount overall.", expected_query="SELECT * FROM orders ORDER BY amount DESC LIMIT 1;", hint="ORDER BY amount DESC LIMIT 1", solution="SELECT * FROM orders ORDER BY amount DESC LIMIT 1;")
    ])

    # ------------------ Level 4: NULL Handling (20 Questions) ------------------
    l4 = Lesson(level=4, title="Level 4: NULL Handling", content="""
### 🔹 The "Nothingness": Handling NULLs

In SQL, `NULL` represents missing or unknown data. It is **not** the same as zero or an empty string.

#### 1. IS NULL / IS NOT NULL
Because `NULL` is unknown, you cannot use `=` to compare it. Instead, you must use `IS NULL`.
*   **Correct**: `WHERE email IS NULL`
*   **Incorrect**: `WHERE email = NULL` (This will return nothing!)

#### 2. Why it matters
Missing data can break your logic. For example, if you're calculating average age, `NULL` values are typically ignored by aggregate functions.

---
**💡 High-Frequency Interview Question**: "What is the difference between 0, NULL, and an empty string?"
**Answer**: NULL is 'missing data', 0 is a number, and "" is a defined (but empty) text string.
""")
    db.add(l4)
    db.flush()
    db.add_all([
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users without a country.", expected_query="SELECT * FROM users WHERE country IS NULL;", hint="IS NULL", solution="SELECT * FROM users WHERE country IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users who HAVE a country.", expected_query="SELECT * FROM users WHERE country IS NOT NULL;", hint="IS NOT NULL", solution="SELECT * FROM users WHERE country IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find payments where status is NULL.", expected_query="SELECT * FROM payments WHERE payment_status IS NULL;", hint="IS NULL", solution="SELECT * FROM payments WHERE payment_status IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find products with no name.", expected_query="SELECT * FROM products WHERE name IS NULL;", hint="IS NULL", solution="SELECT * FROM products WHERE name IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="List all non-null emails.", expected_query="SELECT * FROM users WHERE email IS NOT NULL;", hint="IS NOT NULL", solution="SELECT * FROM users WHERE email IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Count users with NULL country.", expected_query="SELECT COUNT(*) FROM users WHERE country IS NULL;", hint="COUNT + WHERE", solution="SELECT COUNT(*) FROM users WHERE country IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find orders with no user ID linked.", expected_query="SELECT * FROM orders WHERE user_id IS NULL;", hint="IS NULL", solution="SELECT * FROM orders WHERE user_id IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users where both country and age are NOT NULL.", expected_query="SELECT * FROM users WHERE country IS NOT NULL AND age IS NOT NULL;", hint="Combine with AND", solution="SELECT * FROM users WHERE country IS NOT NULL AND age IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find payments where payment_method is NULL.", expected_query="SELECT * FROM payments WHERE payment_method IS NULL;", hint="IS NULL", solution="SELECT * FROM payments WHERE payment_method IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="List product IDs with NULL category.", expected_query="SELECT id FROM products WHERE category IS NULL;", hint="IS NULL", solution="SELECT id FROM products WHERE category IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users where age is NULL.", expected_query="SELECT * FROM users WHERE age IS NULL;", hint="IS NULL", solution="SELECT * FROM users WHERE age IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find orders where amount IS NOT NULL.", expected_query="SELECT * FROM orders WHERE amount IS NOT NULL;", hint="IS NOT NULL", solution="SELECT * FROM orders WHERE amount IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Count payments with NULL status.", expected_query="SELECT COUNT(*) FROM payments WHERE payment_status IS NULL;", hint="COUNT", solution="SELECT COUNT(*) FROM payments WHERE payment_status IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users without email OR without country.", expected_query="SELECT * FROM users WHERE email IS NULL OR country IS NULL;", hint="Use OR", solution="SELECT * FROM users WHERE email IS NULL OR country IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find products with price NOT NULL and name NOT NULL.", expected_query="SELECT * FROM products WHERE price IS NOT NULL AND name IS NOT NULL;", hint="Use AND", solution="SELECT * FROM products WHERE price IS NOT NULL AND name IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="List all orders having user_id.", expected_query="SELECT id FROM orders WHERE user_id IS NOT NULL;", hint="IS NOT NULL", solution="SELECT id FROM orders WHERE user_id IS NOT NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users whose country is NULL but age is > 18.", expected_query="SELECT * FROM users WHERE country IS NULL AND age > 18;", hint="Combine", solution="SELECT * FROM users WHERE country IS NULL AND age > 18;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find any product with price as NULL.", expected_query="SELECT * FROM products WHERE price IS NULL;", hint="IS NULL", solution="SELECT * FROM products WHERE price IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Find users where name is NULL.", expected_query="SELECT * FROM users WHERE name IS NULL;", hint="IS NULL", solution="SELECT * FROM users WHERE name IS NULL;"),
        Question(lesson_id=l4.id, question_type="challenge", question_text="Count total rows where any field is NULL (simulated).", expected_query="SELECT COUNT(*) FROM users WHERE country IS NULL OR age IS NULL;", hint="OR logic", solution="SELECT COUNT(*) FROM users WHERE country IS NULL OR age IS NULL;")
    ])

    # ------------------ Level 5: Aggregation (20 Questions) ------------------
    l5 = Lesson(level=5, title="Level 5: Aggregation", content="""
### 🔹 Crunching Numbers: Aggregates & Grouping

This is where SQL becomes a powerful business tool. Aggregations allow you to summarize thousands of rows into a single number.

#### 1. Basic Functions
*   **COUNT()**: Number of rows.
*   **SUM()**: Total of a numeric column.
*   **AVG()**: Average value.
*   **MAX() / MIN()**: Highest and lowest values.

#### 2. GROUP BY
Groups rows that have the same values into summary rows.
*   **Syntax**: `SELECT country, COUNT(*) FROM users GROUP BY country;`

#### 3. HAVING
The `WHERE` clause for groups. Use it when you need to filter *after* aggregation.
*   **Syntax**: `SELECT ... GROUP BY country HAVING COUNT(*) > 10;`

---
**💡 Golden Rule**: You cannot use `WHERE` to filter aggregate results; you **must** use `HAVING`.
""")
    db.add(l5)
    db.flush()
    db.add_all([
        Question(lesson_id=l5.id, question_type="challenge", question_text="Count total users.", expected_query="SELECT COUNT(*) FROM users;", hint="COUNT", solution="SELECT COUNT(*) FROM users;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find avg product price.", expected_query="SELECT AVG(price) FROM products;", hint="AVG", solution="SELECT AVG(price) FROM products;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Total revenue (SUM of order amounts).", expected_query="SELECT SUM(amount) FROM orders;", hint="SUM", solution="SELECT SUM(amount) FROM orders;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Count users per country.", expected_query="SELECT country, COUNT(*) FROM users GROUP BY country;", hint="GROUP BY", solution="SELECT country, COUNT(*) FROM users GROUP BY country;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find categories with > 10 products.", expected_query="SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) > 10;", hint="HAVING", solution="SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) > 10;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Max price per category.", expected_query="SELECT category, MAX(price) FROM products GROUP BY category;", hint="GROUP BY", solution="SELECT category, MAX(price) FROM products GROUP BY category;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Total spent by user ID 5.", expected_query="SELECT SUM(amount) FROM orders WHERE user_id = 5;", hint="SUM with WHERE", solution="SELECT SUM(amount) FROM orders WHERE user_id = 5;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Average age of users from India.", expected_query="SELECT AVG(age) FROM users WHERE country = 'India';", hint="AVG with WHERE", solution="SELECT AVG(age) FROM users WHERE country = 'India;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Count orders per status.", expected_query="SELECT status, COUNT(*) FROM orders GROUP BY status;", hint="GROUP BY", solution="SELECT status, COUNT(*) FROM orders GROUP BY status;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Min and Max order amount.", expected_query="SELECT MIN(amount), MAX(amount) FROM orders;", hint="MIN, MAX", solution="SELECT MIN(amount), MAX(amount) FROM orders;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find users with more than 3 orders.", expected_query="SELECT user_id, COUNT(*) FROM orders GROUP BY user_id HAVING COUNT(*) > 3;", hint="HAVING", solution="SELECT user_id, COUNT(*) FROM orders GROUP BY user_id HAVING COUNT(*) > 3;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Sum of quantity sold per product id.", expected_query="SELECT product_id, SUM(quantity) FROM order_items GROUP BY product_id;", hint="SUM", solution="SELECT product_id, SUM(quantity) FROM order_items GROUP BY product_id;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Count distinct countries in users table.", expected_query="SELECT COUNT(DISTINCT country) FROM users;", hint="COUNT DISTINCT", solution="SELECT COUNT(DISTINCT country) FROM users;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Average quantity in order items.", expected_query="SELECT AVG(quantity) FROM order_items;", hint="AVG", solution="SELECT AVG(quantity) FROM order_items;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find total payments per method.", expected_query="SELECT payment_method, COUNT(*) FROM payments GROUP BY payment_method;", hint="GROUP BY", solution="SELECT payment_method, COUNT(*) FROM payments GROUP BY payment_method;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Sum of price for 'Toys'.", expected_query="SELECT SUM(price) FROM products WHERE category = 'Toys';", hint="SUM with WHERE", solution="SELECT SUM(price) FROM products WHERE category = 'Toys';"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find max quantity in a single order item.", expected_query="SELECT MAX(quantity) FROM order_items;", hint="MAX", solution="SELECT MAX(quantity) FROM order_items;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Find total revenue from 'USA' (simulated with WHERE if users has country, otherwise need join). Let's do revenue from 'completed' status.", expected_query="SELECT SUM(amount) FROM orders WHERE status = 'completed';", hint="SUM WHERE", solution="SELECT SUM(amount) FROM orders WHERE status = 'completed';"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Average order amount.", expected_query="SELECT AVG(amount) FROM orders;", hint="AVG", solution="SELECT AVG(amount) FROM orders;"),
        Question(lesson_id=l5.id, question_type="challenge", question_text="Count how many 'credit_card' payments failed.", expected_query="SELECT COUNT(*) FROM payments WHERE payment_method = 'credit_card' AND payment_status = 'failed';", hint="COUNT with AND", solution="SELECT COUNT(*) FROM payments WHERE payment_method = 'credit_card' AND payment_status = 'failed';")
    ])

    # ------------------ Level 6: Joins (20 Questions) ------------------
    l6 = Lesson(level=6, title="Level 6: SQL Joins", content="""
### 🔹 SQL Joins: The Interview Gold Mine

Joins are used to combine rows from two or more tables, based on a related column between them. This is the **#1 most asked** category in technical interviews.

#### 1. INNER JOIN
Returns records that have matching values in **both** tables.
*   **Scenario**: Get only users who have actually placed an order.
*   **Syntax**: `SELECT * FROM users JOIN orders ON users.id = orders.user_id;`

#### 2. LEFT (OUTER) JOIN
Returns **all** records from the left table, and the matched records from the right table. If there's no match, the right side is `NULL`.
*   **Scenario**: List all users, including those who have never ordered anything.
*   **Syntax**: `SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id;`

#### 3. RIGHT (OUTER) JOIN
Returns **all** records from the right table, and the matched records from the left table.
*   **Native Support**: Now fully supported by our PostgreSQL backend!
*   **Syntax**: `SELECT * FROM users RIGHT JOIN orders ON users.id = orders.user_id;`

#### 4. FULL (OUTER) JOIN
Returns **all** records when there is a match in either left or right table.
*   **Scenario**: A complete list of all users and all orders, matched where possible.
*   **Native Support**: Now fully supported!

---
**💡 Pro Tip**: Always specify the table name (e.g., `users.id`) when joining to avoid "ambiguous column name" errors!
""")
    db.add(l6)
    db.flush()
    db.add_all([
        Question(lesson_id=l6.id, question_type="challenge", question_text="List all user names and their order amounts.", expected_query="SELECT users.name, orders.amount FROM users JOIN orders ON users.id = orders.user_id;", hint="JOIN users and orders", solution="SELECT users.name, orders.amount FROM users JOIN orders ON users.id = orders.user_id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find user names and total spent by each.", expected_query="SELECT users.name, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;", hint="JOIN + SUM + GROUP BY", solution="SELECT users.name, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List products and the quantity sold of each.", expected_query="SELECT products.name, SUM(order_items.quantity) FROM products JOIN order_items ON products.id = order_items.product_id GROUP BY products.id;", hint="JOIN + SUM", solution="SELECT products.name, SUM(order_items.quantity) FROM products JOIN order_items ON products.id = order_items.product_id GROUP BY products.id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find users who have NOT placed any orders (using LEFT JOIN).", expected_query="SELECT users.name FROM users LEFT JOIN orders ON users.id = orders.user_id WHERE orders.id IS NULL;", hint="LEFT JOIN where ID IS NULL", solution="SELECT users.name FROM users LEFT JOIN orders ON users.id = orders.user_id WHERE orders.id IS NULL;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List each product and its category for items in order ID 10.", expected_query="SELECT products.name, products.category FROM products JOIN order_items ON products.id = order_items.product_id WHERE order_items.order_id = 10;", hint="JOIN with WHERE", solution="SELECT products.name, products.category FROM products JOIN order_items ON products.id = order_items.product_id WHERE order_items.order_id = 10;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find payment method used for each order ID.", expected_query="SELECT orders.id, payments.payment_method FROM orders JOIN payments ON orders.id = payments.order_id;", hint="JOIN orders and payments", solution="SELECT orders.id, payments.payment_method FROM orders JOIN payments ON orders.id = payments.order_id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List all users from India and their order statuses.", expected_query="SELECT users.name, orders.status FROM users JOIN orders ON users.id = orders.user_id WHERE users.country = 'India';", hint="JOIN with WHERE", solution="SELECT users.name, orders.status FROM users JOIN orders ON users.id = orders.user_id WHERE users.country = 'India';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find the most expensive product bought by user with name 'John Doe'.", expected_query="SELECT MAX(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id WHERE users.name = 'John Doe';", hint="Triple JOIN", solution="SELECT MAX(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id WHERE users.name = 'John Doe';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List order IDs and the count of items in each (join products for extra info).", expected_query="SELECT order_items.order_id, COUNT(*) FROM order_items GROUP BY order_id;", hint="Actually just aggregation, but interviews ask it with join often. Let's do: SELECT o.id, COUNT(oi.id) FROM orders o JOIN order_items oi ON o.id = oi.order_id GROUP BY o.id", solution="SELECT orders.id, COUNT(order_items.id) FROM orders JOIN order_items ON orders.id = order_items.order_id GROUP BY orders.id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find total revenue per category.", expected_query="SELECT products.category, SUM(orders.amount) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.category;", hint="JOIN 3 tables + SUM", solution="SELECT products.category, SUM(orders.amount) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.category;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Show order date, user name, and order amount for top 5 largest orders.", expected_query="SELECT orders.created_at, users.name, orders.amount FROM orders JOIN users ON orders.user_id = users.id ORDER BY orders.amount DESC LIMIT 5;", hint="JOIN + ORDER BY + LIMIT", solution="SELECT orders.created_at, users.name, orders.amount FROM orders JOIN users ON orders.user_id = users.id ORDER BY orders.amount DESC LIMIT 5;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List users who paid with 'credit_card'.", expected_query="SELECT DISTINCT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN payments ON orders.id = payments.order_id WHERE payments.payment_method = 'credit_card';", hint="Triple JOIN", solution="SELECT DISTINCT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN payments ON orders.id = payments.order_id WHERE payments.payment_method = 'credit_card';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find the average price of products bought by users from Brazil.", expected_query="SELECT AVG(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id WHERE users.country = 'Brazil';", hint="Triple JOIN + AVG", solution="SELECT AVG(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id WHERE users.country = 'Brazil';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Check if any order has multiple payment status entries (self-simulated). For now, list all orders and their payment statuses.", expected_query="SELECT orders.id, payments.payment_status FROM orders JOIN payments ON orders.id = payments.order_id;", hint="JOIN", solution="SELECT orders.id, payments.payment_status FROM orders JOIN payments ON orders.id = payments.order_id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find user names who bought something in 'Electronics' category.", expected_query="SELECT DISTINCT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics';", hint="Triple JOIN + DISTINCT", solution="SELECT DISTINCT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find the total quantity of 'Toys' sold.", expected_query="SELECT SUM(order_items.quantity) FROM order_items JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys';", hint="JOIN + SUM", solution="SELECT SUM(order_items.quantity) FROM order_items JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys';"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List all products and the count of unique users who bought them.", expected_query="SELECT products.name, COUNT(DISTINCT orders.user_id) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.id;", hint="JOIN + COUNT DISTINCT + GROUP BY", solution="SELECT products.name, COUNT(DISTINCT orders.user_id) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.id;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Average amount of orders made by users aged 18-25.", expected_query="SELECT AVG(orders.amount) FROM orders JOIN users ON orders.user_id = users.id WHERE users.age BETWEEN 18 AND 25;", hint="JOIN + WHERE BETWEEN + AVG", solution="SELECT AVG(orders.amount) FROM orders JOIN users ON orders.user_id = users.id WHERE users.age BETWEEN 18 AND 25;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="Find revenue per country from 'completed' orders.", expected_query="SELECT users.country, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id WHERE orders.status = 'completed' GROUP BY users.country;", hint="JOIN + WHERE + GROUP BY", solution="SELECT users.country, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id WHERE orders.status = 'completed' GROUP BY users.country;"),
        Question(lesson_id=l6.id, question_type="challenge", question_text="List each product name and the user who most recently bought it (simple JOIN version).", expected_query="SELECT products.name, users.name FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id ORDER BY orders.created_at DESC;", hint="Triple JOIN + ORDER BY", solution="SELECT products.name, users.name FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id JOIN users ON orders.user_id = users.id ORDER BY orders.created_at DESC;")
    ])

    # ------------------ Level 7: Subqueries & EXISTS (20 Questions) ------------------
    l7 = Lesson(level=7, title="Level 7: Subqueries & EXISTS", content="""
### 🔹 Queries Within Queries: Subqueries & EXISTS

A subquery is a SQL query nested inside a larger query. It’s like a mathematical expression where you calculate a value first, then use it in the main formula.

#### 1. Scalar Subqueries
Returns a single value. Often used in the `WHERE` clause for comparison.
*   **Example**: `SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);`

#### 2. Correlated Subqueries
A subquery that uses values from the outer query. It is evaluated once for each row processed by the outer query.
*   **Performance Note**: These can be slow on very large datasets!

#### 3. EXISTS / NOT EXISTS
Used to check if a subquery returns any rows. It’s often faster than `IN` for large datasets.
*   **Scenario**: Find users who have placed **at least one** order.
*   **Syntax**: `SELECT name FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id);`

---
**💡 Interview Tip**: If an interviewer asks how to find 'the highest salary without using MAX()', they are looking for a subquery solution!
""")
    db.add(l7)
    db.flush()
    db.add_all([
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find users who have at least one order.", expected_query="SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);", hint="Use IN with subquery", solution="SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find users who have placed NO orders.", expected_query="SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM orders);", hint="Use NOT IN", solution="SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM orders);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="List names of users using EXISTS.", expected_query="SELECT name FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id);", hint="EXISTS (...) ", solution="SELECT name FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find products with price higher than average.", expected_query="SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);", hint="WHERE price > (SELECT AVG...)", solution="SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find names of users who bought 'Toys' category products.", expected_query="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys');", hint="Subquery with JOINS", solution="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys');"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find orders greater than the average order amount.", expected_query="SELECT * FROM orders WHERE amount > (SELECT AVG(amount) FROM orders);", hint="Compare to AVG subquery", solution="SELECT * FROM orders WHERE amount > (SELECT AVG(amount) FROM orders);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="List products that have never been ordered.", expected_query="SELECT * FROM products WHERE id NOT IN (SELECT product_id FROM order_items);", hint="NOT IN", solution="SELECT * FROM products WHERE id NOT IN (SELECT product_id FROM order_items);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Users who spent the most (highest single order amount).", expected_query="SELECT * FROM users WHERE id = (SELECT user_id FROM orders ORDER BY amount DESC LIMIT 1);", hint="Subquery with LIMIT 1", solution="SELECT * FROM users WHERE id = (SELECT user_id FROM orders ORDER BY amount DESC LIMIT 1);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find categories with at least one product > 500.", expected_query="SELECT DISTINCT category FROM products WHERE category IN (SELECT category FROM products WHERE price > 500);", hint="Simple subquery", solution="SELECT DISTINCT category FROM products WHERE category IN (SELECT category FROM products WHERE price > 500);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Count users from countries where at least one user is older than 50.", expected_query="SELECT COUNT(*) FROM users WHERE country IN (SELECT country FROM users WHERE age > 50);", hint="Nested filter", solution="SELECT COUNT(*) FROM users WHERE country IN (SELECT country FROM users WHERE age > 50);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="List user IDs who used 'credit_card' in payments.", expected_query="SELECT id FROM users WHERE id IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id WHERE payments.payment_method = 'credit_card');", hint="JOIN in subquery", solution="SELECT id FROM users WHERE id IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id WHERE payments.payment_method = 'credit_card');"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find orders from users from USA (using subquery).", expected_query="SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE country = 'United States');", hint="Subquery filtering by country", solution="SELECT * FROM orders WHERE user_id IN (SELECT id FROM users WHERE country = 'United States');"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Get average price of products in 'Toys' vs others (using subquery).", expected_query="SELECT AVG(price) FROM products WHERE category = 'Toys';", hint="Simple version", solution="SELECT AVG(price) FROM products WHERE category = 'Toys';"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find users who have at least one payment.", expected_query="SELECT * FROM users WHERE id IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id);", hint="Subquery with JOIN", solution="SELECT * FROM users WHERE id IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find users who have NO payments records.", expected_query="SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id);", hint="NOT IN + JOIN", solution="SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM orders JOIN payments ON orders.id = payments.order_id);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="List product names with quantity sold > 10.", expected_query="SELECT name FROM products WHERE id IN (SELECT product_id FROM order_items GROUP BY product_id HAVING SUM(quantity) > 10);", hint="Subquery with GROUP BY/HAVING", solution="SELECT name FROM products WHERE id IN (SELECT product_id FROM order_items GROUP BY product_id HAVING SUM(quantity) > 10);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find users from India who spent more than $1000 in total.", expected_query="SELECT * FROM users WHERE country = 'India' AND id IN (SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 1000);", hint="Subquery with HAVING", solution="SELECT * FROM users WHERE country = 'India' AND id IN (SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 1000);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find the most sold product name.", expected_query="SELECT name FROM products WHERE id = (SELECT product_id FROM order_items GROUP BY product_id ORDER BY SUM(quantity) DESC LIMIT 1);", hint="Subquery with ORDER BY SUM", solution="SELECT name FROM products WHERE id = (SELECT product_id FROM order_items GROUP BY product_id ORDER BY SUM(quantity) DESC LIMIT 1);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Is there any user who bought all products? (simulated). Find users with same count of bought products as total products.", expected_query="SELECT user_id FROM (SELECT user_id, COUNT(DISTINCT product_id) as cnt FROM orders JOIN order_items ON orders.id = order_items.order_id GROUP BY user_id) WHERE cnt = (SELECT COUNT(*) FROM products);", hint="Nested subquery count", solution="SELECT user_id FROM (SELECT user_id, COUNT(DISTINCT product_id) as cnt FROM orders JOIN order_items ON orders.id = order_items.order_id GROUP BY user_id) WHERE cnt = (SELECT COUNT(*) FROM products);"),
        Question(lesson_id=l7.id, question_type="challenge", question_text="Find the average age of users who bought 'Pro' products.", expected_query="SELECT AVG(age) FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.name LIKE '%Pro%');", hint="Subquery with LIKE and JOIN", solution="SELECT AVG(age) FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.name LIKE '%Pro%');")
    ])

    # ------------------ Level 8: Advanced Logic (20 Questions) ------------------
    l8 = Lesson(level=8, title="Level 8: Advanced Logic", content="""
### 🔹 Conditional Mastery: CASE & Date Functions

Level 8 bridges the gap between simple data retrieval and business logic.

#### 1. CASE Statement
The `IF-THEN-ELSE` of SQL. It allows you to create new categories on the fly.
*   **Syntax**:
    ```sql
    SELECT name,
    CASE
        WHEN age < 18 THEN 'Minor'
        WHEN age >= 18 THEN 'Adult'
        ELSE 'Unknown'
    END AS status
    FROM users;
    ```

#### 2. Date & Time Functions
Handling dates is notoriously tricky. Common functions include `CURRENT_DATE`, `DATE_PART` (or `strftime` in SQLite/Postgres).
*   **Example**: `SELECT * FROM orders WHERE created_at > NOW() - INTERVAL '30 days';`

---
**💡 Pro Tip**: Use `CASE` inside an `ORDER BY` to create custom sorting logic (e.g., specific status priority)!
""")
    db.add(l8)
    db.flush()
    db.add_all([
        Question(lesson_id=l8.id, question_type="challenge", question_text="Categorize users into 'Minor' (<18) or 'Adult' (>=18).", expected_query="SELECT name, CASE WHEN age < 18 THEN 'Minor' ELSE 'Adult' END as category FROM users;", hint="Use CASE", solution="SELECT name, CASE WHEN age < 18 THEN 'Minor' ELSE 'Adult' END as category FROM users;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Categorize products as 'Cheap' (<20), 'Medium' (20-100), or 'Premium' (>100).", expected_query="SELECT name, CASE WHEN price < 20 THEN 'Cheap' WHEN price BETWEEN 20 AND 100 THEN 'Medium' ELSE 'Premium' END as price_range FROM products;", hint="Multi-WHEN CASE", solution="SELECT name, CASE WHEN price < 20 THEN 'Cheap' WHEN price BETWEEN 20 AND 100 THEN 'Medium' ELSE 'Premium' END as price_range FROM products;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find the month of each order (SQLite).", expected_query="SELECT id, strftime('%m', created_at) as month FROM orders;", hint="Use strftime", solution="SELECT id, strftime('%m', created_at) as month FROM orders;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Show total revenue per month.", expected_query="SELECT strftime('%m', created_at) as month, SUM(amount) FROM orders GROUP BY month;", hint="GROUP BY strftime", solution="SELECT strftime('%m', created_at) as month, SUM(amount) FROM orders GROUP BY month;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find the number of days since each user registered (simulated).", expected_query="SELECT name, (julianday('now') - julianday(created_at)) as days FROM users;", hint="Use julianday", solution="SELECT name, (julianday('now') - julianday(created_at)) as days FROM users;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="List users and label those from India as 'Local' and others as 'International'.", expected_query="SELECT name, CASE WHEN country = 'India' THEN 'Local' ELSE 'International' END as origin FROM users;", hint="Simple CASE", solution="SELECT name, CASE WHEN country = 'India' THEN 'Local' ELSE 'International' END as origin FROM users;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find which status has the most average order amount.", expected_query="SELECT status, AVG(amount) as avg_amt FROM orders GROUP BY status ORDER BY avg_amt DESC LIMIT 1;", hint="GROUP BY + ORDER BY", solution="SELECT status, AVG(amount) as avg_amt FROM orders GROUP BY status ORDER BY avg_amt DESC LIMIT 1;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Identify orders placed on weekends (Sat=6, Sun=0 in some systems, SQLite %w: 0-6 Sun-Sat).", expected_query="SELECT * FROM orders WHERE strftime('%w', created_at) IN ('0', '6');", hint="strftime('%w')", solution="SELECT * FROM orders WHERE strftime('%w', created_at) IN ('0', '6');"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Calculate total orders for only users who have 'gmail' in their email.", expected_query="SELECT COUNT(*) FROM orders WHERE user_id IN (SELECT id FROM users WHERE email LIKE '%gmail%');", hint="Subquery filter", solution="SELECT COUNT(*) FROM orders WHERE user_id IN (SELECT id FROM users WHERE email LIKE '%gmail%');"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Show order amount alongside the average amount of ALL orders.", expected_query="SELECT id, amount, (SELECT AVG(amount) FROM orders) as global_avg FROM orders;", hint="Scalar subquery", solution="SELECT id, amount, (SELECT AVG(amount) FROM orders) as global_avg FROM orders;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="List each product and its percentage of total revenue.", expected_query="SELECT product_id, SUM(amount) * 100.0 / (SELECT SUM(amount) FROM orders) as pct FROM orders JOIN order_items ON orders.id = order_items.order_id GROUP BY product_id;", hint="Complex calculation", solution="SELECT product_id, SUM(amount) * 100.0 / (SELECT SUM(amount) FROM orders) as pct FROM orders JOIN order_items ON orders.id = order_items.order_id GROUP BY product_id;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Count how many payments were made in each year.", expected_query="SELECT strftime('%Y', created_at) as year, COUNT(*) FROM payments GROUP BY year;", hint="strftime %Y", solution="SELECT strftime('%Y', created_at) as year, COUNT(*) FROM payments GROUP BY year;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find the user who placed their most recent order today (if any).", expected_query="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE date(created_at) = date('now'));", hint="date('now')", solution="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders WHERE date(created_at) = date('now'));"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Label orders as 'Big' (>500) or 'Small' otherwise.", expected_query="SELECT id, CASE WHEN amount > 500 THEN 'Big' ELSE 'Small' END as type FROM orders;", hint="CASE", solution="SELECT id, CASE WHEN amount > 500 THEN 'Big' ELSE 'Small' END as type FROM orders;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find revenue per payment status.", expected_query="SELECT payment_status, SUM(orders.amount) FROM payments JOIN orders ON payments.order_id = orders.id GROUP BY payment_status;", hint="JOIN + GROUP BY", solution="SELECT payment_status, SUM(orders.amount) FROM payments JOIN orders ON payments.order_id = orders.id GROUP BY payment_status;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Select users who joined in January of any year.", expected_query="SELECT * FROM users WHERE strftime('%m', created_at) = '01';", hint="strftime %m = 01", solution="SELECT * FROM users WHERE strftime('%m', created_at) = '01';"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="List products and their status: 'Out of Stock' (never ordered) or 'In Stock'.", expected_query="SELECT name, CASE WHEN id IN (SELECT product_id FROM order_items) THEN 'In Stock' ELSE 'Out of Stock' END as status FROM products;", hint="CASE with IN subquery", solution="SELECT name, CASE WHEN id IN (SELECT product_id FROM order_items) THEN 'In Stock' ELSE 'Out of Stock' END as status FROM products;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find total quantity sold per month.", expected_query="SELECT strftime('%m', orders.created_at) as month, SUM(quantity) FROM order_items JOIN orders ON order_items.order_id = orders.id GROUP BY month;", hint="JOIN + strftime", solution="SELECT strftime('%m', orders.created_at) as month, SUM(quantity) FROM order_items JOIN orders ON order_items.order_id = orders.id GROUP BY month;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Show user name, and 'Top Spender' if their total amount > 5000.", expected_query="SELECT name, CASE WHEN id IN (SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 5000) THEN 'Top Spender' ELSE 'Regular' END as badge FROM users;", hint="CASE with subquery", solution="SELECT name, CASE WHEN id IN (SELECT user_id FROM orders GROUP BY user_id HAVING SUM(amount) > 5000) THEN 'Top Spender' ELSE 'Regular' END as badge FROM users;"),
        Question(lesson_id=l8.id, question_type="challenge", question_text="Find the gap in years between registration and latest order per user.", expected_query="SELECT users.id, (strftime('%Y', MAX(orders.created_at)) - strftime('%Y', users.created_at)) as years_gap FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;", hint="MAX(created_at) and date diff", solution="SELECT users.id, (strftime('%Y', MAX(orders.created_at)) - strftime('%Y', users.created_at)) as years_gap FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;")
    ])

    # ------------------ Level 9: UNION (20 Questions) ------------------
    l9 = Lesson(level=9, title="Level 9: UNION", content="""
### 🔹 Stacking Results: UNION & UNION ALL

`UNION` is used to combine the result-set of two or more `SELECT` statements.

#### 1. UNION vs. UNION ALL
*   **UNION**: Removes duplicate rows between the sets. (Slower due to sorting/deduplication).
*   **UNION ALL**: Keeps every row, including duplicates. (Faster).

#### 2. The Rules
- Each `SELECT` statement must have the same number of columns.
- The columns must have similar data types.
- The columns must be in the same order.

---
**💡 Scenario**: Combining a list of 'Prospects' and 'Customers' into a single mailing list.
""")
    db.add(l9)
    db.flush()
    db.add_all([
        Question(lesson_id=l9.id, question_type="challenge", question_text="Combine all names from users and products.", expected_query="SELECT name FROM users UNION SELECT name FROM products;", hint="UNION", solution="SELECT name FROM users UNION SELECT name FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Combine emails and names in one list.", expected_query="SELECT name FROM users UNION ALL SELECT email FROM users;", hint="UNION ALL", solution="SELECT name FROM users UNION ALL SELECT email FROM users;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="List Indian countries and Brazilian countries in one set.", expected_query="SELECT DISTINCT country FROM users WHERE country = 'India' UNION SELECT DISTINCT country FROM users WHERE country = 'Brazil';", hint="UNION with filtering", solution="SELECT DISTINCT country FROM users WHERE country = 'India' UNION SELECT DISTINCT country FROM users WHERE country = 'Brazil';"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Get user IDs and product IDs (stacked).", expected_query="SELECT id FROM users UNION SELECT id FROM products;", hint="UNION IDs", solution="SELECT id FROM users UNION SELECT id FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="List all statuses from orders and payments.", expected_query="SELECT status FROM orders UNION SELECT payment_status FROM payments;", hint="UNION statuses", solution="SELECT status FROM orders UNION SELECT payment_status FROM payments;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Fetch users from USA UNION users from Canada.", expected_query="SELECT * FROM users WHERE country = 'United States' UNION SELECT * FROM users WHERE country = 'Canada';", hint="UNION two selects", solution="SELECT * FROM users WHERE country = 'United States' UNION SELECT * FROM users WHERE country = 'Canada';"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="List names of users and products, adding a 'type' column.", expected_query="SELECT name, 'User' as type FROM users UNION SELECT name, 'Product' as type FROM products;", hint="Static type column", solution="SELECT name, 'User' as type FROM users UNION SELECT name, 'Product' as type FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Identify all distinct values across different tables (complex).", expected_query="SELECT country FROM users UNION SELECT category FROM products;", hint="UNION random columns", solution="SELECT country FROM users UNION SELECT category FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Show order amount UNION payment amount (stacked).", expected_query="SELECT amount FROM orders UNION SELECT amount FROM payments JOIN orders ON orders.id = payments.order_id;", hint="UNION amounts", solution="SELECT amount FROM orders UNION SELECT amount FROM payments JOIN orders ON orders.id = payments.order_id;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="List all user IDs minus those who ordered? (SQLite EXCEPT).", expected_query="SELECT id FROM users EXCEPT SELECT user_id FROM orders;", hint="Use EXCEPT", solution="SELECT id FROM users EXCEPT SELECT user_id FROM orders;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Find common category names and user names? (INTERSECT).", expected_query="SELECT name FROM users INTERSECT SELECT category FROM products;", hint="Use INTERSECT", solution="SELECT name FROM users INTERSECT SELECT category FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Union of Top 3 users and Bottom 3 users by age.", expected_query="SELECT * FROM (SELECT * FROM users ORDER BY age DESC LIMIT 3) UNION SELECT * FROM (SELECT * FROM users ORDER BY age ASC LIMIT 3);", hint="UNION of subqueries", solution="SELECT * FROM (SELECT * FROM users ORDER BY age DESC LIMIT 3) UNION SELECT * FROM (SELECT * FROM users ORDER BY age ASC LIMIT 3);"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Union of most expensive product and cheapest product.", expected_query="SELECT * FROM (SELECT * FROM products ORDER BY price DESC LIMIT 1) UNION SELECT * FROM (SELECT * FROM products ORDER BY price ASC LIMIT 1);", hint="UNION LIMIT cases", solution="SELECT * FROM (SELECT * FROM products ORDER BY price DESC LIMIT 1) UNION SELECT * FROM (SELECT * FROM products ORDER BY price ASC LIMIT 1);"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="All order items IDs and all payment IDs.", expected_query="SELECT id FROM order_items UNION SELECT id FROM payments;", hint="UNION", solution="SELECT id FROM order_items UNION SELECT id FROM payments;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Distinct category names from products and statuses from orders.", expected_query="SELECT category FROM products UNION SELECT status FROM orders;", hint="UNION", solution="SELECT category FROM products UNION SELECT status FROM orders;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Combine name and category into one column.", expected_query="SELECT name FROM users UNION SELECT category FROM products;", hint="UNION", solution="SELECT name FROM users UNION SELECT category FROM products;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="List unique amounts across orders and payments.", expected_query="SELECT amount FROM orders UNION SELECT amount FROM payments JOIN orders ON orders.id = payments.order_id;", hint="UNION", solution="SELECT amount FROM orders UNION SELECT amount FROM payments JOIN orders ON orders.id = payments.order_id;"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="IDs of pending orders UNION IDs of failed payments.", expected_query="SELECT id FROM orders WHERE status = 'pending' UNION SELECT id FROM payments WHERE payment_status = 'failed';", hint="UNION filtered selects", solution="SELECT id FROM orders WHERE status = 'pending' UNION SELECT id FROM payments WHERE payment_status = 'failed';"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Combine name filters: start with 'A' and start with 'Z'.", expected_query="SELECT * FROM users WHERE name LIKE 'A%' UNION SELECT * FROM users WHERE name LIKE 'Z%';", hint="UNION LIKEs", solution="SELECT * FROM users WHERE name LIKE 'A%' UNION SELECT * FROM users WHERE name LIKE 'Z%';"),
        Question(lesson_id=l9.id, question_type="challenge", question_text="Most recent user and most recent product ID.", expected_query="SELECT id FROM users ORDER BY created_at DESC LIMIT 1 UNION SELECT id FROM products ORDER BY id DESC LIMIT 1;", hint="UNION recent records", solution="SELECT id FROM users ORDER BY created_at DESC LIMIT 1 UNION SELECT id FROM products ORDER BY id DESC LIMIT 1;")
    ])

    # ------------------ Level 10: Final Challenges (20 Questions) ------------------
    l10 = Lesson(level=10, title="Level 10: Final Challenges", content="""
### 🔹 The Finish Line: Grand Mastery

Welcome to Level 10. There are no new commands here—only survival.

#### What to Expect:
- **Triple & Quadruple Joins**: Connecting entire database schemas.
- **Nested Aggregations**: Finding the average of a sum grouped by a category.
- **Complex Logic**: Combining `CASE`, `EXISTS`, and `UNION` in a single query.

#### Interview Mindset:
When faced with a complex problem, **break it down**. Use `WITH` clauses (CTEs) or temporary logic to solve pieces of the puzzle before assembling the final query.

---
**🏆 Achievement Unlocked**: If you solve these 20 questions, you are technically ready for Mid-Level Data Analyst interviews!
""")
    db.add(l10)
    db.flush()
    db.add_all([
        Question(lesson_id=l10.id, question_type="challenge", question_text="Calculate total revenue per country, identifying countries with total revenue exceeding 5000.", expected_query="SELECT users.country, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.country HAVING SUM(orders.amount) > 5000;", hint="Multiple requirements", solution="SELECT users.country, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.country HAVING SUM(orders.amount) > 5000;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Identify the user who has spent the most on products in the 'Electronics' category.", expected_query="SELECT users.name, SUM(orders.amount) as total FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics' GROUP BY users.id ORDER BY total DESC LIMIT 1;", hint="4 table join, aggregation, sorting", solution="SELECT users.name, SUM(orders.amount) as total FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics' GROUP BY users.id ORDER BY total DESC LIMIT 1;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="List users who have placed orders for products in both 'Electronics' and 'Toys' categories.", expected_query="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics') AND id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys');", hint="Double subquery or INTERSECT", solution="SELECT name FROM users WHERE id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Electronics') AND id IN (SELECT user_id FROM orders JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id WHERE products.category = 'Toys');"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find the ratio of successful payments to total payments.", expected_query="SELECT (SELECT COUNT(*) FROM payments WHERE payment_status = 'success') * 100.0 / (SELECT COUNT(*) FROM payments);", hint="Scalar subquery calculation", solution="SELECT (SELECT COUNT(*) FROM payments WHERE payment_status = 'success') * 100.0 / (SELECT COUNT(*) FROM payments);"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="List the most recent order for each user with at least one order.", expected_query="SELECT users.name, MAX(orders.created_at) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;", hint="JOIN + GROUP BY + MAX", solution="SELECT users.name, MAX(orders.created_at) FROM users JOIN orders ON users.id = orders.user_id GROUP BY users.id;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find the top 3 categories by total revenue and the average product price in each of those categories.", expected_query="SELECT products.category, SUM(orders.amount), AVG(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.category ORDER BY SUM(orders.amount) DESC LIMIT 3;", hint="Advanced aggregation", solution="SELECT products.category, SUM(orders.amount), AVG(products.price) FROM products JOIN order_items ON products.id = order_items.product_id JOIN orders ON order_items.order_id = orders.id GROUP BY products.category ORDER BY SUM(orders.amount) DESC LIMIT 3;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find users who have spent more than the average expenditure of users from their same country (tricky).", expected_query="SELECT u1.name FROM users u1 JOIN orders o1 ON u1.id = o1.user_id GROUP BY u1.id HAVING SUM(o1.amount) > (SELECT AVG(spent) FROM (SELECT SUM(amount) as spent FROM users u2 JOIN orders o2 ON u2.id = o2.user_id WHERE u2.country = u1.country GROUP BY u2.id));", hint="Correlated subquery or self-reference", solution="SELECT u1.name FROM users u1 JOIN orders o1 ON u1.id = o1.user_id GROUP BY u1.id HAVING SUM(o1.amount) > (SELECT AVG(spent) FROM (SELECT SUM(amount) as spent FROM users u2 JOIN orders o2 ON u2.id = o2.user_id WHERE u2.country = u1.country GROUP BY u2.id));"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Identify orders where the total items quantity is greater than 10.", expected_query="SELECT order_id FROM order_items GROUP BY order_id HAVING SUM(quantity) > 10;", hint="Aggregating by order_id", solution="SELECT order_id FROM order_items GROUP BY order_id HAVING SUM(quantity) > 10;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find the user who has ordered from the highest number of unique categories.", expected_query="SELECT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id GROUP BY users.id ORDER BY COUNT(DISTINCT products.category) DESC LIMIT 1;", hint="Multiple joins and DISTINCT count", solution="SELECT users.name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id GROUP BY users.id ORDER BY COUNT(DISTINCT products.category) DESC LIMIT 1;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Calculate the year-over-year revenue growth percentage (approximate with existing data).", expected_query="SELECT strftime('%Y', created_at) as yr, SUM(amount) FROM orders GROUP BY yr;", hint="Simple growth list", solution="SELECT strftime('%Y', created_at) as yr, SUM(amount) FROM orders GROUP BY yr;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Identify products that are frequently bought together (same order). List product pairs.", expected_query="SELECT a.product_id, b.product_id FROM order_items a JOIN order_items b ON a.order_id = b.order_id WHERE a.product_id < b.product_id GROUP BY a.product_id, b.product_id ORDER BY COUNT(*) DESC LIMIT 10;", hint="Self-join pattern", solution="SELECT a.product_id, b.product_id FROM order_items a JOIN order_items b ON a.order_id = b.order_id WHERE a.product_id < b.product_id GROUP BY a.product_id, b.product_id ORDER BY COUNT(*) DESC LIMIT 10;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find users who made multiple payments for the same order (simulated).", expected_query="SELECT order_id, COUNT(*) FROM payments GROUP BY order_id HAVING COUNT(*) > 1;", hint="Grouping with HAVING", solution="SELECT order_id, COUNT(*) FROM payments GROUP BY order_id HAVING COUNT(*) > 1;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Determine the most popular payment method in each country (tricky join).", expected_query="SELECT users.country, payments.payment_method, COUNT(*) as cnt FROM users JOIN orders ON users.id = orders.user_id JOIN payments ON orders.id = payments.order_id GROUP BY users.country, payments.payment_method ORDER BY cnt DESC;", hint="Multi-group sort", solution="SELECT users.country, payments.payment_method, COUNT(*) as cnt FROM users JOIN orders ON users.id = orders.user_id JOIN payments ON orders.id = payments.order_id GROUP BY users.country, payments.payment_method ORDER BY cnt DESC;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Identify products that represent 80% of total revenue (Pareto analysis). List revenue per product.", expected_query="SELECT product_id, SUM(amount) as rev FROM order_items JOIN orders ON order_items.order_id = orders.id GROUP BY product_id ORDER BY rev DESC;", hint="List sorted revenue", solution="SELECT product_id, SUM(amount) as rev FROM order_items JOIN orders ON order_items.order_id = orders.id GROUP BY product_id ORDER BY rev DESC;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find orders where the amount is within 10% of the maximum order amount.", expected_query="SELECT * FROM orders WHERE amount >= (SELECT MAX(amount) * 0.9 FROM orders);", hint="Scalar subquery math", solution="SELECT * FROM orders WHERE amount >= (SELECT MAX(amount) * 0.9 FROM orders);"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Select users who joined in the same month as their most recent order.", expected_query="SELECT name FROM users WHERE strftime('%m', created_at) = (SELECT strftime('%m', MAX(created_at)) FROM orders WHERE orders.user_id = users.id);", hint="Correlated subquery", solution="SELECT name FROM users WHERE strftime('%m', created_at) = (SELECT strftime('%m', MAX(created_at)) FROM orders WHERE orders.user_id = users.id);"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Calculate average days between consecutive orders for each user (complex).", expected_query="SELECT user_id, AVG(julianday(created_at) - julianday(prev_date)) FROM (SELECT user_id, created_at, (SELECT MAX(created_at) FROM orders o2 WHERE o2.user_id = o1.user_id AND o2.created_at < o1.created_at) as prev_date FROM orders o1) WHERE prev_date IS NOT NULL GROUP BY user_id;", hint="Analytical self-subquery", solution="SELECT user_id, AVG(julianday(created_at) - julianday(prev_date)) FROM (SELECT user_id, created_at, (SELECT MAX(created_at) FROM orders o2 WHERE o2.user_id = o1.user_id AND o2.created_at < o1.created_at) as prev_date FROM orders o1) WHERE prev_date IS NOT NULL GROUP BY user_id;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find the top 3 most profitable products (price - cost, assuming cost=0.5*price).", expected_query="SELECT name, (price * 0.5 * SUM(quantity)) as profit FROM products JOIN order_items ON products.id = order_items.product_id GROUP BY products.id ORDER BY profit DESC LIMIT 3;", hint="Calculated profit sort", solution="SELECT name, (price * 0.5 * SUM(quantity)) as profit FROM products JOIN order_items ON products.id = order_items.product_id GROUP BY products.id ORDER BY profit DESC LIMIT 3;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="Find users who have only bought from a single category.", expected_query="SELECT name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id GROUP BY users.id HAVING COUNT(DISTINCT products.category) = 1;", hint="Grouping with HAVING count=1", solution="SELECT name FROM users JOIN orders ON users.id = orders.user_id JOIN order_items ON orders.id = order_items.order_id JOIN products ON order_items.product_id = products.id GROUP BY users.id HAVING COUNT(DISTINCT products.category) = 1;"),
        Question(lesson_id=l10.id, question_type="challenge", question_text="The ultimate challenge: Find the country with the highest user retention rate (orders in multiple years).", expected_query="SELECT country FROM (SELECT country, user_id FROM users JOIN orders ON users.id = orders.user_id GROUP BY country, user_id HAVING COUNT(DISTINCT strftime('%Y', orders.created_at)) > 1) GROUP BY country ORDER BY COUNT(*) DESC LIMIT 1;", hint="Nested grouping", solution="SELECT country FROM (SELECT country, user_id FROM users JOIN orders ON users.id = orders.user_id GROUP BY country, user_id HAVING COUNT(DISTINCT strftime('%Y', orders.created_at)) > 1) GROUP BY country ORDER BY COUNT(*) DESC LIMIT 1;")
    ])

    # Final User
    u = AppUser(username="dev_student")
    db.add(u)
    db.commit()
    db.close()
    print("Content DB Fully Seeded with 200 Interview Questions!")

if __name__ == "__main__":
    seed_content()
