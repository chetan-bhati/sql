from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_app_db
from app.models_app import Lesson, Example, Question

router = APIRouter()

@router.get("/levels")
def get_levels(db: Session = Depends(get_app_db)):
    """Returns a list of all available levels."""
    lessons = db.query(Lesson).order_by(Lesson.level).all()
    return {"levels": [{"id": l.id, "level": l.level, "title": l.title} for l in lessons]}

@router.get("/lesson/{level}")
def get_lesson(level: int, db: Session = Depends(get_app_db)):
    lesson = db.query(Lesson).filter(Lesson.level == level).first()
    if not lesson: raise HTTPException(404, "Level not found")
    return {"level": lesson.level, "title": lesson.title, "content": lesson.content}

@router.get("/examples/{level}")
def get_examples(level: int, db: Session = Depends(get_app_db)):
    lesson = db.query(Lesson).filter(Lesson.level == level).first()
    if not lesson: raise HTTPException(404, "Level not found")
    return {"examples": [{"query": e.query, "explanation": e.explanation} for e in lesson.examples]}

@router.get("/questions/{level}")
def get_questions(level: int, db: Session = Depends(get_app_db)):
    lesson = db.query(Lesson).filter(Lesson.level == level).first()
    if not lesson: raise HTTPException(404, "Level not found")
    qs = []
    for q in lesson.questions:
        qs.append({
            "id": q.id,
            "question_text": q.question_text,
            "question_type": q.question_type,
            "hint": q.hint
        })
    return {"questions": qs}

@router.get("/solution/{question_id}")
def get_solution(question_id: int, db: Session = Depends(get_app_db)):
    q = db.query(Question).filter(Question.id == question_id).first()
    if not q: raise HTTPException(404, "Question not found")
    return {"solution": q.solution}
