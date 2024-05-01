VENV=.venv
BIN=$(VENV)/bin

install:
	$(BIN)/pip install -r requirements.txt

run-demo-bot:
	$(BIN)/python demo-bot/demo-bot.py

run-catalog-api:
	$(BIN)/uvicorn catalog-api.app.main:app --port=8000 --reload --reload-dir catalog-api

run-email-api:
	$(BIN)/uvicorn email-api.app.main:app --port=8001 --reload --reload-dir email-api
