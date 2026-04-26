import re
import time
from sqlalchemy import text
from app.database import practice_engine_ro

def is_safe_query(query: str) -> bool:
    dangerous_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "CREATE", "GRANT", "REVOKE"]
    upper_query = query.upper()
    for kw in dangerous_keywords:
        if re.search(r'\b' + kw + r'\b', upper_query):
            return False
    return True

def get_common_mistakes(query: str) -> str:
    q_up = query.upper()
    if "SELECT" not in q_up:
        return "Missing SELECT clause."
    if "FROM" not in q_up:
        return "Missing FROM clause."
    return ""

def run_query(query: str):
    if not is_safe_query(query):
        return {"success": False, "error": "Unsafe query detected. Only SELECT statements are allowed.", "columns": [], "rows": []}

    try:
        with practice_engine_ro.connect() as conn:
            result = conn.execute(text(query))
            columns = list(result.keys())
            rows = [list(row) for row in result.fetchall()]
            return {"success": True, "columns": columns, "rows": rows}
    except Exception as e:
        err = str(e)
        mistake = get_common_mistakes(query)
        if mistake:
            err = mistake + " " + err
        return {"success": False, "error": err, "columns": [], "rows": []}

def validate_query(user_query: str, expected_query: str):
    start_time = time.time()
    user_result = run_query(user_query)
    exec_time = (time.time() - start_time) * 1000
    user_result["execution_time_ms"] = round(exec_time, 2)

    if not user_result["success"]:
        user_result["is_correct"] = False
        mistakes = get_common_mistakes(user_query)
        if mistakes and mistakes not in user_result["error"]:
            user_result["error"] = mistakes + " " + user_result["error"]
        return user_result

    expected_result = run_query(expected_query)
    if not expected_result["success"]:
        return {"success": False, "is_correct": False, "error": "Internal error: Expected query failed.", "columns": [], "rows": [], "execution_time_ms": round(exec_time, 2)}

    user_rows_sorted = sorted([str(r) for r in user_result["rows"]])
    expected_rows_sorted = sorted([str(r) for r in expected_result["rows"]])

    if user_rows_sorted == expected_rows_sorted:
        user_result["is_correct"] = True
        user_result["message"] = "Correct! The result matches the expected output."
    else:
        user_result["is_correct"] = False
        mistake = ""
        if len(user_result["columns"]) != len(expected_result["columns"]):
            mistake = f"You selected {len(user_result['columns'])} columns instead of {len(expected_result['columns'])}. "
        user_result["message"] = mistake + "Incorrect. The data returned doesn't match the expected outcome."

    return user_result
