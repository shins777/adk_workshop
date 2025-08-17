# Dockerfile
FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PORT 8080

CMD ["python", "remote_server.py"]
