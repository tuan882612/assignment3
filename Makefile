.PHONY: run

run:
	@python src/main.py

clean:
	@find . \( -name '__pycache__' -o -name '*.pyc' -o -name '*.pyo' \) -delete