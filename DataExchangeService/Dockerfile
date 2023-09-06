FROM python:latest
WORKDIR /app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY . .

EXPOSE 5433
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]