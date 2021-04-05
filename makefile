CLI := docker run -it --rm wpbindt/genetic-algorithm

build-image :
	docker build -qt wpbindt/genetic-algorithm .
test :
	make build-image
	$(CLI) python3 -m pytest
mypy :
	make build-image
	$(CLI) mypy tests src scripts
