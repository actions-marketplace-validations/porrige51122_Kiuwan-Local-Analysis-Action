# Runs the given python file
run:
	@echo "\033[92m==> Running kla.py... \033[0m"
	@python3 ./kla.py || true
	@rm -rf ./tmp

# Installs the tools needed for this make file to work
tools:
	@echo "\033[92m==> Installing external tools\033[0m"
	pip install black==22.3.0
	pip install pytest==7.1.2
	pip install pytest-mock==3.7.0

# Formats the code automatically
fmt:
	@echo "\033[92m==> Fixing source code with black\033[0m"
	@black .

# Checks the code for formatting errors
fmtcheck:
	@echo "\033[92m==> Checking source code with black\033[0m"
	@black --check . || (echo; \
		echo "Errors found in files"; \
		echo "To automatically fix the misspelling, run 'make fmt'"; \
		exit 1)

# Runs the testing suite using pytest
test: tools fmt
	@echo "\033[92m==> Testing\033[0m"
	@rm -rf ./test
	pytest

# Runs the testing suite but with console output on all tests (easier for debugging and skips installing tools every time)
test_clear:
	@echo "\033[92m==> Testing\033[0m"
	@rm -rf ./test
	pytest -rP

.PHONY: tools fmt fmtcheck test test_clear
