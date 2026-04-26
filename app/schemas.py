from pydantic import BaseModel
from typing import List, Optional, Any

class QuerySubmit(BaseModel):
    query: str
    question_id: int

class QueryResult(BaseModel):
    success: bool
    is_correct: Optional[bool] = None
    message: Optional[str] = None
    error: Optional[str] = None
    columns: List[str] = []
    rows: List[List[Any]] = []
    execution_time_ms: Optional[float] = None
    attempts: Optional[int] = None
