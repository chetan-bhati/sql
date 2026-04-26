from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import BaseApp

class AppUser(BaseApp):
    __tablename__ = "app_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

class Lesson(BaseApp):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True, index=True)
    level = Column(Integer, unique=True, index=True)
    title = Column(String)
    content = Column(Text) # HTML / Markdown
    
    examples = relationship("Example", back_populates="lesson", cascade="all, delete-orphan")
    questions = relationship("Question", back_populates="lesson", cascade="all, delete-orphan")

class Example(BaseApp):
    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    query = Column(Text)
    explanation = Column(Text)
    
    lesson = relationship("Lesson", back_populates="examples")

class Question(BaseApp):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    question_text = Column(Text)
    expected_query = Column(Text)
    hint = Column(Text)
    solution = Column(Text)
    question_type = Column(String, default="challenge") # 'guided' or 'challenge'
    
    lesson = relationship("Lesson", back_populates="questions")

class UserProgress(BaseApp):
    __tablename__ = "user_progress"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("app_users.id"))
    level = Column(Integer)
    completed = Column(Boolean, default=False)
