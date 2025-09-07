.PHONY: help setup test lint format clean

help:
	@echo "Common targets:"
	@echo "  setup   - create conda env and install package (editable)"
	@echo "  test    - run a quick import test"
	@echo "  lint    - run basic lint (ruff if installed)"
	@echo "  format  - auto-format with black (if installed)"
	@echo "  clean   - remove caches and build artifacts"

setup:
	mamba env create -f environment.yml || conda env create -f environment.yml
	@echo "Activate with: conda activate ionthefold"

test:
	python -c "import ionthefold, sys; print('ionthefold OK')"

lint:
	ruff check src || true

format:
	black src || true

clean:
	rm -rf __pycache__ */__pycache__ .pytest_cache build dist *.egg-info
