from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_app_db
from app.models_app import AppUser

router = APIRouter()

@router.get("/progress")
def get_progress(db: Session = Depends(get_app_db)):
    user = db.query(AppUser).filter(AppUser.username == "dev_student").first()
    if not user:
        user = AppUser(username="dev_student", current_level=1)
        db.add(user)
        db.commit()
        db.refresh(user)
        
    return {"username": user.username, "current_level": user.current_level}

@router.post("/reset")
def reset_progress(db: Session = Depends(get_app_db)):
    user = db.query(AppUser).filter(AppUser.username == "dev_student").first()
    if user:
        user.current_level = 1
        db.commit()
    return {"message": "Progress reset to Level 1"}
