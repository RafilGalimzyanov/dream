from typing import List
from pydantic import BaseModel, Field


class Response(BaseModel):
    row: dict = Field(None, description="Ответ от сервиса BadlistedWordsDetector")