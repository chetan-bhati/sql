# SQL Learning Platform

A complete platform to learn and practice SQL step-by-step using a real fast backend written in FastAPI and SQLAlchemy.

## Features Let Users:
1. Progress through up to 10 levels of SQL logic.
2. Formulate and run queries safely against a mock database with ~1000 records.
3. Automatically validate their query outputs to see if they solved the problem correctly!

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite (for internal DB and read-only practice DB)
- Pydantic
- Simple pure HTML + JS Web UI (included at `/`)

## Setup & Running Locally

1. **Activate the Virtual Environment**
   Make sure you are in the project folder, then run:
   ```bash
   source venv/bin/activate
   ```

2. **Wait, you need to seed the Database initially?**
   The database has been seeded for you automatically to `./data/practice.db` containing Users, Orders, Products, and OrderItems.

3. **Run the fast API server**
   ```bash
   python3 run.py
   ```
   Or use uvicorn explicitly:
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Start Learning!**
   Open your browser and navigate to:
   [http://localhost:8000/](http://localhost:8000/) - The main learning platform UI.
   [http://localhost:8000/docs](http://localhost:8000/docs) - The OpenAPI Swagger specification.

Enjoy mastering SQL directly from your browser!
