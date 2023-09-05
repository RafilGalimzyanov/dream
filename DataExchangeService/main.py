from fastapi import FastAPI
from pydantic import json
from starlette.responses import JSONResponse

from DataExchangeService.app.process import processing_data
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


@app.post("/test", tags=["Tag_name"], response_model=JSONResponse,
          summary="Тестовый метод", description="Тест",
          )
async def get_categories(
        data: json
):
    return await processing_data(data)
