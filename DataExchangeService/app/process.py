import aiohttp
import json

from .db import DatabaseWriter


async def processing_data(data: dict):
    writer = DatabaseWriter()

    try:
        writer.add_request_info(data)  # Добавляем данные в RequestInfo

        url = 'http://badlisted-words:8018/badlisted_words'
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(data)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=json_data, headers=headers) as response:
                answer_data = await response.json()
                if answer_data:
                    writer.add_answer_info(answer_data)  # Добавляем данные в AnswerInfo
                    return answer_data
    except Exception as e:
        print(f"Error during processing: {e}")

    return {}
