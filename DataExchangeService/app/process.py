import aiohttp
import json

from .db import DataBase


async def processing_data(data: dict):
    await DataBase().connect()

    await DataBase.add_request_info(data)

    async with aiohttp.ClientSession() as session:
        url = 'http://badlisted-words:8018/badlisted_words'
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(data)

        answer_data = None
        async with session.post(url, data=json_data, headers=headers) as response:
            answer_data = await response.json()

    if answer_data:
        await DataBase.add_answer_info(answer_data)
        return answer_data
    await DataBase.close()

    return {}
