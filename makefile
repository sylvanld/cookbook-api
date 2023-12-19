
VENV:=.venv

COOKBOOK_API_PORT ?= 8032
COOKBOOK_API_URL ?= http://localhost:$(COOKBOOK_API_PORT)

export

.DEFAULT_GOAL=help

$(VENV):
	virtualenv -p python3 $(VENV)

requires-venv:
	@[ -d $(VENV) ] || make install


help: ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[$$()% 0-9a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development targets

install: $(VENV) ## Install development dependencies in a virtualenv
	$(VENV)/bin/pip install -r requirements/dev.txt

lock: ## Pin latest versions of dependencies compatible with requirements/prod in requirements/lock file
	virtualenv -p python3 .tmp-venv
	.tmp-venv/bin/pip install -r requirements/prod.txt
	.tmp-venv/bin/pip freeze > requirements/lock.txt
	rm -rf .tmp-venv

format: requires-venv ## Format code according to project conventions
	$(VENV)/bin/isort cookbook tests
	$(VENV)/bin/black --line-length 120 cookbook tests

serve: requires-venv ## Start API server in debug mode
	$(VENV)/bin/uvicorn --host 0.0.0.0 --port $(COOKBOOK_API_PORT) cookbook.__main__:api --reload

VENOM_VAR_COOKBOOK_API_URL := $(COOKBOOK_API_URL)
target=.*.yml
test-e2e:  ## Run end to end tests
	@for file in `find tests/e2e/ -type f -regextype egrep -regex '$(target)$$' | sort`; \
		do venom run -vvv $$file; \
		done

##@ Docker targets

build: ## Build docker image
	@docker build -t sylvanld/cookbook-api:latest .
