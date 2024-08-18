.PHONY: clean run test setup help

# Run the application
run:
	python scripts/run_app.py

# Set up the project environment
setup:
	pip install -r requirements.txt

# Clean up .pyc files and __pycache__ directories
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

# Display help information
help:
	@echo "Available commands:"
	@echo "  make run       - Run the application"
	@echo "  make setup     - Set up the project environment"
	@echo "  make clean     - Clean up .pyc files and __pycache__ directories"

# Default target
all: setup test run

# Clean and run
clean-run: clean run