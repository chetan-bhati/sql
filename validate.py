from app.services.sql_runner import run_query, validate_query
from app.content import LEVELS
from app.database import get_app_db, AppSessionLocal, BaseApp, app_engine
from app.models_app import AppUser

BaseApp.metadata.create_all(bind=app_engine)

print("1. Testing Levels Dictionary...")
assert len(LEVELS) == 10, "There should be 10 levels"
assert len(LEVELS[1]["questions"]) > 0

print("2. Testing SQL Engine with proper query...")
expected = LEVELS[1]["questions"][0]["expected_query"]
print(f"   Executing: {expected}")
res = run_query(expected)
assert res["success"] == True, "Expected query should succeed"
# We seeded 1000 users, check length
print(f"   Fetched {len(res['rows'])} rows with columns: {res['columns']}")
assert len(res['rows']) == 1000, "Should have returned 1000 users"

print("3. Testing exact SQL validation...")
val_res = validate_query(expected, expected)
assert val_res["success"] == True
assert val_res["is_correct"] == True
print("   Validation matched perfectly!")

print("4. Testing invalid query matching...")
val_bad = validate_query("SELECT id, name FROM users LIMIT 5", expected)
assert val_bad["is_correct"] == False
print(f"   Failed match correctly detected: {val_bad['message']}")

print("5. Testing SQL injection / dangerous keywords...")
unsafe_res = run_query("DROP TABLE users;")
assert unsafe_res["success"] == False
assert "Unsafe query detected" in unsafe_res["error"]
print("   Blocked unsafe drop query!")

print("6. Testing internal App Database...")
db = AppSessionLocal()
u = db.query(AppUser).filter(AppUser.username == "dev_student").first()
if not u:
    u = AppUser(username="dev_student")
    db.add(u)
    db.commit()

from app.models_app import UserProgress
p = db.query(UserProgress).filter(UserProgress.user_id == u.id).first()
print(f"   Fetched App user: {u.username}, level 1 completed: {p.completed if p else 'no progress'}")
db.close()

print("ALL TESTS PASSED ✨")
