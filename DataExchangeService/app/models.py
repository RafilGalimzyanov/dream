from typing import List
from pydantic import BaseModel, Field


class AnswerData(BaseModel):
    row: List[dict] = Field(None, description="Ответ от сервиса BadlistedWordsDetector")