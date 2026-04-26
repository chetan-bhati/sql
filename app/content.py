LEVELS = {
    1: {
        "title": "Level 1: The Basics (SELECT & WHERE)",
        "description": "Learn to fetch data and use basic filtering.",
        "questions": [
            {
                "id": 1,
                "text": "Fetch all columns from the users table.",
                "expected_query": "SELECT * FROM users;"
            },
            {
                "id": 2,
                "text": "Find the names and emails of all users.",
                "expected_query": "SELECT name, email FROM users;"
            },
            {
                "id": 3,
                "text": "Find users who are exactly 25 years old.",
                "expected_query": "SELECT * FROM users WHERE age = 25;"
            }
        ]
    },
    2: {
        "title": "Level 2: Advanced Filtering",
        "description": "Learn LIKE, IN, NOT IN, and BETWEEN.",
        "questions": [
            {
                "id": 4,
                "text": "Find users whose email ends with '@example.com'.",
                "expected_query": "SELECT * FROM users WHERE email LIKE '%@example.com';"
            },
            {
                "id": 5,
                "text": "Find products in the 'Electronics' or 'Books' category.",
                "expected_query": "SELECT * FROM products WHERE category IN ('Electronics', 'Books');"
            },
            {
                "id": 6,
                "text": "Find orders with an amount between 50 and 150.",
                "expected_query": "SELECT * FROM orders WHERE amount BETWEEN 50 AND 150;"
            }
        ]
    },
    3: {
        "title": "Level 3: Sorting & Limiting",
        "description": "Learn ORDER BY and LIMIT.",
        "questions": [
            {
                "id": 7,
                "text": "Find the top 5 most expensive products.",
                "expected_query": "SELECT * FROM products ORDER BY price DESC LIMIT 5;"
            },
            {
                "id": 8,
                "text": "Fetch the 10 oldest users.",
                "expected_query": "SELECT * FROM users ORDER BY age DESC LIMIT 10;"
            }
        ]
    },
    4: {
        "title": "Level 4: NULL Handling",
        "description": "Learn IS NULL and IS NOT NULL.",
        "questions": [
            {
                "id": 9,
                "text": "Find users whose country is NOT known (assuming country might be NULL usually, but let's just query where country is null).",
                "expected_query": "SELECT * FROM users WHERE country IS NULL;"
            }
        ]
    },
    5: {
        "title": "Level 5: Aggregation",
        "description": "Learn COUNT, SUM, AVG, GROUP BY.",
        "questions": [
            {
                "id": 10,
                "text": "Count the total number of users.",
                "expected_query": "SELECT COUNT(*) FROM users;"
            },
            {
                "id": 11,
                "text": "Find the average price of products in each category.",
                "expected_query": "SELECT category, AVG(price) FROM products GROUP BY category;"
            }
        ]
    },
    6: {
        "title": "Level 6: Joins",
        "description": "Learn INNER JOIN and LEFT JOIN.",
        "questions": [
            {
                "id": 12,
                "text": "List all order IDs and the names of the users who placed them.",
                "expected_query": "SELECT orders.id, users.name FROM orders INNER JOIN users ON orders.user_id = users.id;"
            },
            {
                "id": 13,
                "text": "List user names and their order amounts, including users without orders.",
                "expected_query": "SELECT users.name, orders.amount FROM users LEFT JOIN orders ON users.id = orders.user_id;"
            }
        ]
    },
    7: {
        "title": "Level 7: Advanced Queries",
        "description": "Learn UNION, EXISTS, and ANY/ALL.",
        "questions": [
            {
                "id": 14,
                "text": "Find the names of users who have placed an order (using EXISTS).",
                "expected_query": "SELECT name FROM users WHERE EXISTS (SELECT 1 FROM orders WHERE orders.user_id = users.id);"
            }
        ]
    },
    8: {
        "title": "Level 8: Data Modification (Read-Only Practice)",
        "description": "Practice writing INSERT, UPDATE, DELETE logic (these won't change DB).",
        "questions": [
            {
                "id": 15,
                "text": "Write a query to mark all pending orders as completed (NOTE: This will trigger the safety check in the execution engine in real use, so we just return syntax checks or explain usually). For this practice, we just ask for SELECT syntax of finding those first.",
                "expected_query": "SELECT * FROM orders WHERE status = 'pending';"
            }
        ]
    },
    9: {
        "title": "Level 9: Schema & Index",
        "description": "Theory of schemas and indices.",
        "questions": [
            {
                "id": 16,
                "text": "Select the name of the 'users' table columns (using SQLite pragma or standard select). Let's just find the names of users from USA.",
                "expected_query": "SELECT name FROM users WHERE country = 'United States';"
            }
        ]
    },
    10: {
        "title": "Level 10: Final Challenge",
        "description": "Advanced problem solving.",
        "questions": [
            {
                "id": 17,
                "text": "Find the total revenue generated by each user, showing user name and total amount.",
                "expected_query": "SELECT users.name, SUM(orders.amount) FROM users JOIN orders ON users.id = orders.user_id WHERE orders.status = 'completed' GROUP BY users.name;"
            }
        ]
    }
}
