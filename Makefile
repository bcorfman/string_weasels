SHELL := env PYTHON_VERSION=3.9 /bin/bash
.SILENT: install devinstall test run
PYTHON_VERSION ?= 3.9

install:
	uv python pin $(PYTHON_VERSION)
	uv sync --no-dev

devinstall:
	uv python pin $(PYTHON_VERSION)
	uv sync --dev

test:
	uv run pytest

run:
	uv run python weasels.py
