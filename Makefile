VENV=.venv
BIN=$(VENV)/bin

install:
	$(BIN)/pip install -r requirements.txt

run-demo-bot:
	$(BIN)/python demo-bot/demo-bot.py

run-northwind-api:
	$(BIN)/uvicorn northwind-api.app.main:app --port=8000 --reload --reload-dir northwind-api

run-email-api:
	$(BIN)/uvicorn email-api.app.main:app --port=8001 --reload --reload-dir email-api
