from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import inspect, text
from app.database import practice_engine_ro

router = APIRouter()

@router.get("/schema")
def get_schema():
    """Returns the names of all tables and their columns in the practice DB."""
    inspector = inspect(practice_engine_ro)
    tables = inspector.get_table_names()
    
    schema = {}
    for table in tables:
        columns = inspector.get_columns(table)
        schema[table] = [
            {"name": col["name"], "type": str(col["type"])}
            for col in columns
        ]
    
    return {"schema": schema}

@router.get("/table/{table_name}")
def get_table_data(table_name: str):
    """Returns the first 10 rows of a specific table for preview."""
    # Basic protection against SQL injection via table_name
    # Since we use list from inspector, it's safer, but let's be sure.
    inspector = inspect(practice_engine_ro)
    if table_name not in inspector.get_table_names():
        raise HTTPException(status_code=404, detail="Table not found")

    try:
        with practice_engine_ro.connect() as conn:
            # We use text() but with an identifier we checked against the inspector
            query = text(f"SELECT * FROM {table_name} LIMIT 10")
            result = conn.execute(query)
            columns = list(result.keys())
            rows = [list(row) for row in result.fetchall()]
            return {"columns": columns, "rows": rows}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
