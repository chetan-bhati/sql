import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Fallback to SQLite if DATABASE_URL is not set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./internal.db")
PRACTICE_DB_URL = os.getenv("DATABASE_URL", "sqlite:///./data/practice.db")

# For SQLite, we need connect_args={"check_same_thread": False}. 
# For PostgreSQL, we don't.
def get_engine_args(url):
    if url.startswith("sqlite"):
        return {"connect_args": {"check_same_thread": False}}
    return {}

# Create engines
app_engine = create_engine(DATABASE_URL, **get_engine_args(DATABASE_URL))
practice_engine = create_engine(PRACTICE_DB_URL, **get_engine_args(PRACTICE_DB_URL))

# Read-only engine for safe practice query execution
if PRACTICE_DB_URL.startswith("sqlite"):
    practice_ro_url = f"sqlite:///file:{os.path.abspath('./data/practice.db')}?mode=ro&uri=true"
    practice_engine_ro = create_engine(practice_ro_url, connect_args={"check_same_thread": False})
else:
    # For PostgreSQL, we use the same engine but we rely on the DB user or other safeguards if needed.
    # For now, we use the same URL but can be constrained later.
    practice_engine_ro = practice_engine

# Session locals
AppSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=app_engine)
PracticeSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=practice_engine)

BaseApp = declarative_base()
BasePractice = declarative_base()

# Dependencies
def get_app_db():
    db = AppSessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_practice_db():
    db = PracticeSessionLocal()
    try:
        yield db
    finally:
        db.close()
