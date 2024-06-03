FROM python:3.9-slim AS base

RUN useradd -ms /bin/bash appuser

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

ENV PORT=8001

EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
