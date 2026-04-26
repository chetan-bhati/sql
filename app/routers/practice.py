from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import QuerySubmit, QueryResult
from app.services.sql_runner import validate_query
from app.database import get_app_db
from app.models_app import AppUser, Question, UserProgress

router = APIRouter()

# In-memory dictionary to count attempts (simple temporary solution)
attempt_tracker = {}

@router.post("/submit-query", response_model=QueryResult)
def submit_query(payload: QuerySubmit, db: Session = Depends(get_app_db)):
    question = db.query(Question).filter(Question.id == payload.question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
        
    global attempt_tracker
    track_key = f"user_1_q_{payload.question_id}"
    attempt_tracker[track_key] = attempt_tracker.get(track_key, 0) + 1
    
    result = validate_query(payload.query, question.expected_query)
    result["attempts"] = attempt_tracker[track_key]
    
    if result.get("is_correct"):
        user = db.query(AppUser).filter(AppUser.username == "dev_student").first()
        if not user:
            user = AppUser(username="dev_student")
            db.add(user)
            db.commit()
            
        prog = db.query(UserProgress).filter(UserProgress.user_id == user.id, UserProgress.level == question.lesson_id).first()
        if not prog:
            prog = UserProgress(user_id=user.id, level=question.lesson_id)
            db.add(prog)
        prog.completed = True
        db.commit()
    
    return result
