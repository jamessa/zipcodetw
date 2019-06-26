install:
	pip install -v -e .
clean:
	rm -rf .venv/
	git clean -df
db:
	python3 -m zipcodetw.builder
venv:
	virtualenv --python=python3 .venv
