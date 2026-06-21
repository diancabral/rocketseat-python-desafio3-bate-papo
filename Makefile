.PHONY: help install run clean

.DEFAULT_GOAL := help

VENV := .venv
PY := $(VENV)/bin/python
ACTIVATE := $(VENV)/bin/activate

help:
	@echo "Available commands:"
	@echo "  make install      - install dependencies (uv sync into $(VENV))"
	@echo "  make run          - activate $(VENV) and run the API (creates $(VENV) and installs deps if needed)"
	@echo "  make clean        - remove __pycache__ directories and .pyc files"

install:
	uv sync

run:
	@if [ -x "$(PY)" ]; then \
		echo "Using virtual environment $(VENV)"; \
		. "$(ACTIVATE)" && PYTHONPATH=src python src/app.py; \
	else \
		echo "Creating $(VENV) and installing dependencies..."; \
		uv venv "$(VENV)" && uv sync && . "$(ACTIVATE)" && PYTHONPATH=src python src/app.py; \
	fi

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete 2>/dev/null || true
