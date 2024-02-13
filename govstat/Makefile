.PHONY: help test
help:
	@echo "usage: make <option>"
	@echo "options and effects:"
	@echo "    help                     : Show help"
	@echo "    test                     : Test ..."

test:
	@echo "test ..."
	echo $(conda info --base)

.PHONY: activate create-requirements import-sql
activate:
	@echo "conda activate china-administrative-division"

create-requirements:
	@conda list -e > requirements.txt

import-sql:
	@mysql -u root -p 123456 < govstat.sql

.PHONY: export
export:
	@python ./tool/export.py

.PHONY: crawl-province crawl-city crawl-county crawl-town crawl-village
crawl-province:
	@python ./tool/launch_province.py
crawl-city:
	@python ./tool/launch_city.py
crawl-county:
	@python ./tool/launch_county.py
crawl-town:
	@python ./tool/launch_town.py
crawl-village:
	@python ./tool/launch_village.py