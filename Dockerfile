FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
CMD ["fastapi", "dev", "app/main.py", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sleep", "infinity"]