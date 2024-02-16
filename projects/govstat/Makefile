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

.PHONY: crawl-province crawl-city crawl-county crawl-town crawl-village
crawl-province:
	@python launch_province.py
crawl-city:
	@python launch_city.py
crawl-county:
	@python launch_county.py
crawl-town:
	@python launch_town.py
crawl-village:
	@python launch_village.py