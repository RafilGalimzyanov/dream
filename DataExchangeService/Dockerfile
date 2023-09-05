FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5433
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "5433"]