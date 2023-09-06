import json
import os

import asyncpg
from .settings import setting


class DataBase:
    connection = None

    @classmethod
    async def connect(cls):
        if not cls.connection:
            try:
                cls.connection = await asyncpg.connect(
                    user=setting.user_name,
                    password=setting.password,
                    host=os.getenv("DATABASE_HOST"),
                    port=setting.port,
                    database=setting.name
                )

                return True
            except asyncpg.PostgresError as e:
                print(f"Logging error: cannot connect to db, {e}")
                return False

    @classmethod
    async def close(cls):
        try:
            if cls.connection:
                await cls.connection.close()
        finally:
            cls.connection = None

    @classmethod
    async def add_request_info(cls, data):
        try:
            for key, value in data.items():
                await cls.connection.execute("select * from proxy.addrequestinfo($1,$2)", key, json.dumps(value))
        except asyncpg.exceptions.RaiseError as e:
            print(e)

    @classmethod
    async def add_answer_info(cls, answer):
        try:
            await cls.connection.execute("select * from proxy.addanswerinfo($1,$2)", "data", json.dumps(answer))
        except asyncpg.exceptions.RaiseError as e:
            print(e)

