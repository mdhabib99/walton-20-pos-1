# Define targets
clean:
	@$(MAKE) clean-pyc
	@$(MAKE) clean-build
	@$(MAKE) clean-test
	@$(MAKE) clean-ruff
	@echo "All build, test, coverage, and Python artifacts have been removed."

clean-build:
	@rm -rf build/ dist/ .eggs/
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@find . -type f -name "*.egg" -exec rm -f {} +

clean-pyc:
	@find . -type f -name "*.pyc" -exec rm -f {} +
	@find . -type f -name "*.pyo" -exec rm -f {} +
	@find . -type f -name "*~" -exec rm -f {} +
	@find . -type d -name "__pycache__" -exec rm -rf {} +

clean-test:
	@rm -rf .tox/ .coverage htmlcov/ .pytest_cache/

clean-ruff:
	@rm -rf .ruff_cache/

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available targets:"
	@echo "  clean           - Remove all artifacts"
	@echo "  clean-build     - Remove build artifacts"
	@echo "  clean-pyc       - Remove Python artifacts"
	@echo "  clean-test      - Remove test artifacts"
	@echo "  clean-ruff      - Remove the .ruff_cache"
	@echo "  help            - Display this help message"

# This prevents Make from confusing targets with files of the same name.
.PHONY: clean clean-build clean-pyc clean-test help


# run the oddo dev server
run:
	@echo "running server on localhost:8080"
	@./odoo-bin -c ./odoo-dev.conf --update pos_fixed_discount

start:
	@echo "starting production server on localhost:8069"
	@./odoo-bin -c ./odoo.conf