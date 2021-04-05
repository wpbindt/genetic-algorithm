CLI := docker run -it --rm wpbindt/genetic-algorithm

build-image :
	docker build -qt wpbindt/genetic-algorithm .
test : build-image
	$(CLI) python3 -m pytest -q
mypy : build-image
	$(CLI) mypy tests src scripts
