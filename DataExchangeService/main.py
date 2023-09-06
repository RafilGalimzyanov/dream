from fastapi import FastAPI
from pydantic import json
from starlette.responses import JSONResponse

from app.models import Response
from app.process import processing_data
from app import settings


tags_metadata = [
    {
        "name": "Data Exchange",
        "description": "Перенаправление данных с сохранением"
    },
]


app = FastAPI(
    title="DataExchangeService",
    openapi_tags=tags_metadata,
    description="Testing service for redirects data",
    version="0.3.0",
    debug=True,
    root_path=settings.CommonSettings().api_path
)


@app.post("/test", tags=["Tag_name"], response_model=Response,
          summary="Тестовый метод", description="Тест",
          )
async def get_categories(
        data: dict
):
    return await processing_data(data)
