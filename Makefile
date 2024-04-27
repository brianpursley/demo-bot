VENV=.venv
BIN=$(VENV)/bin

install: install-northwind-api install-demo-bot

install-northwind-api:
	$(BIN)/pip install -r northwind-api/requirements.txt

install-demo-bot:
	$(BIN)/pip install -r demo-bot/requirements.txt

run-demo-bot:
	$(BIN)/python demo-bot/demo-bot.py

run-northwind-api:
	$(BIN)/uvicorn northwind-api.app.main:app --reload
