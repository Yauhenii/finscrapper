VENV_NAME = .venv/
BIN_PATH = $(VENV_NAME)bin/
# PYTHON_PATH = $(BIN_PATH)python

venv::
	python3 -m venv $(VENV_NAME); $(BIN_PATH)pip install --upgrade pip;

clear::
	rm -rf $(VENV_NAME)

sync::
	$(BIN_PATH)pip install -r requirements-dev.txt
