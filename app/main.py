import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os

from app.routers import levels, practice, progress, explorer
from app.database import BaseApp, app_engine

# Initialize App DB
BaseApp.metadata.create_all(bind=app_engine)

app = FastAPI(title="SQL Learning Platform")

# Allow easy communication from optional frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(levels.router, prefix="/api", tags=["Levels"])
app.include_router(practice.router, prefix="/api", tags=["Practice"])
app.include_router(progress.router, prefix="/api", tags=["Progress"])
app.include_router(explorer.router, prefix="/api/explorer", tags=["Explorer"])

@app.get("/", response_class=HTMLResponse)
def root():
    if os.path.exists("index.html"):
        with open("index.html", "r") as f:
            return f.read()
    return "<h1>Welcome to the SQL Learning API!</h1><p>Visit /docs to see the API docs, or add an index.html at root to see the frontend.</p>"
