.PHONY: help test
help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help                     : Show help"
	@echo "    test                     : Test ..."

test:
	@echo "test ..."

.PHONY:	push create-api
push:
	@git add .
	git commit -m "脚本自动push"
	git push origin main

create-api:
	@goctl api new alice