GO=go
MAIN_GO_FILE=alice.go
GO_CTL=goctl
TOOL_DIR=./tool

.PHONY: help test
help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help                     : Show help"
	@echo "    test                     : Test ..."

test:
	@echo "test ..."

.PHONY:	dev create-api
dev:
	@${GO} run ${MAIN_GO_FILE} -f etc/alice-api.yaml
	@echo "Dev start ..."
create-api:
	@goctl api new alice

.PHONY: api gen-zero-model
gen-zero-model:
	@${GO_CTL} model mysql datasource --url="root:123456@tcp(192.168.200.253:3400)/govstat" -t="province,city,county,town,village" --dir=./model

api: gen-api format-api validate-api
gen-api:
	@${GO_CTL} api go -api ${TOOL_DIR}/alice.api -dir .
	@echo "Generate api success ..."
format-api:
	@${GO_CTL} api format --dir=${TOOL_DIR}
	@echo "Format api success ..."
validate-api:
	@${GO_CTL} api validate --api=${TOOL_DIR}/province.api
	@${GO_CTL} api validate --api=${TOOL_DIR}/city.api
	@${GO_CTL} api validate --api=${TOOL_DIR}/county.api

.PHONY: gentool-model gen-gorm-model
gentool-model:
	@gentool -c ${TOOL_DIR}/gentool.yaml
gen-gorm-model:
	@${GO} run ${TOOL_DIR}/main.go -f ${TOOL_DIR}/conf.yaml