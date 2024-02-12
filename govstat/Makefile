.PHONY: help test
help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help                     : Show help"
	@echo "    test                     : Test ..."

test:
	@echo "test ..."
	echo $(conda info --base)

.PHONY: activate create-requirements
activate:
	@echo "conda activate china-administrative-division"

create-requirements:
	@conda list -e > requirements.txt

.PHONY: build
build:
	@python ./_export/export.py