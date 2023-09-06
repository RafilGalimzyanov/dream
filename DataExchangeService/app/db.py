import json
import os
import aiohttp
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from .settings import setting

Base = declarative_base()

class RequestInfo(Base):
    __tablename__ = 'request_info'

    id = Column(Integer, primary_key=True)
    key = Column(String)
    value = Column(JSON)

class AnswerInfo(Base):
    __tablename__ = 'answer_info'

    id = Column(Integer, primary_key=True)
    data = Column(JSON)


class DatabaseWriter:
    def __init__(self):
        db_url = f'postgresql://{setting.user_name}:{setting.password}@{os.getenv("DATABASE_HOST")}:{setting.port}/{setting.name}'
        self.engine = create_engine(db_url)
        self.session = Session(self.engine)

    def add_request_info(self, data):
        try:
            for key, value in data.items():
                request_info = RequestInfo(key=key, value=value)
                self.session.add(request_info)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()

    def add_answer_info(self, answer):
        try:
            answer_info = AnswerInfo(data=answer)
            self.session.add(answer_info)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        finally:
            self.session.close()
