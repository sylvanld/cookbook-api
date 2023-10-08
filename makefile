
VENV:=venv

COOKBOOK_DEV_PORT:=8032

$(VENV):
	@python3 -m virtualenv -p python3 $(VENV)
	@echo "Virtualenv created in $(VENV)."
	@echo "Install dependencies with: make install [env=<dev|prod>]"
	exit 1

env=dev
install: $(VENV)
	$(VENV)/bin/pip install -r requirements/$(env).txt

lock:
	python3 -m virtualenv -p python3 tmp-venv
	tmp-venv/bin/pip install -r requirements/prod.txt
	tmp-venv/bin/pip freeze > requirements/lock.txt
	rm -rf tmp-venv

serve: $(VENV)
	$(VENV)/bin/uvicorn --host 0.0.0.0 --port $(COOKBOOK_DEV_PORT) cookbook.__main__:api --reload
