.PHONY: help test lint format migratedb migrate-down migrate-status setup install clean run

help:
	@echo "Lobster AI Assistant - Available Commands"
	@echo "=========================================="
	@echo ""
	@echo "Setup & Installation:"
	@echo "  make setup              Run interactive setup"
	@echo "  make install            Install dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make run                Start the assistant"
	@echo "  make test               Run pytest with coverage"
	@echo "  make lint               Check code quality (flake8, black, isort)"
	@echo "  make format             Auto-format code"
	@echo ""
	@echo "Database:"
	@echo "  make migratedb          Run pending migrations"
	@echo "  make migrate-down       Rollback migrations"
	@echo "  make migrate-status     Show applied migrations"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean              Clean temp files"
	@echo ""

test:
	pytest --cov=src --cov-report=html --cov-report=term-missing

lint:
	flake8 src tests
	black --check src tests
	isort --check-only src tests

format:
	black src tests
	isort src tests

migratedb:
	python -m alembic upgrade head

migrate-down:
	python -m alembic downgrade -1

migrate-status:
	python -m alembic current

setup:
	@echo "Initializing Lobster AI Assistant..."
	@python scripts/setup.py

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

run:
	python -m src.main
