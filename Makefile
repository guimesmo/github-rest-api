SHELL := /bin/sh

export PYTHONPATH := $(pwd)/application

FLASK_APP ?= application/main.py
FLASK_ENV ?= development

.PHONY: runserver runlocal test coverage

runserver:
	cd application && uwsgi --ini ../deployments/uwsgi.ini

runlocal:
	FLASK_APP=$(FLASK_APP) FLASK_ENV=$(FLASK_ENV) python -m flask run

test:
	python -m unittest discover application

coverage:
	coverage run -m unittest discover application
