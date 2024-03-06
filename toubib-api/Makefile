sqlalchemy_url = sqlite:///data/db.sqlite?check_same_thread=false
toubib_api_dir = $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

clean:
	rm -fr data

data:
	mkdir data


# Using poetry

install:
	poetry install

test:
	poetry run pytest --cov toubib --cov tests --cov-report term-missing

check:
	poetry run ruff check

style:
	poetry run ruff format

run-alembic: data
# Upgrade schema and add some fake data
	sqlalchemy_url=$(sqlalchemy_url) poetry run alembic upgrade head

run-api: run-alembic
	sqlalchemy_url=$(sqlalchemy_url) poetry run hypercorn toubib.main:app --reload


# Using docker

docker-build:
	docker build . -t toubib:latest

docker-test: data docker-build
	docker run -t -i -p 8000:8000 -v ${toubib_api_dir}/data:/data toubib:latest pytest --cov toubib --cov tests --cov-report term-missing

docker-run-alembic: data docker-build
	docker run -t -i -v ${toubib_api_dir}/data:/data toubib:latest alembic upgrade head

docker-run-app: docker-run-alembic
	docker run -t -i -p 8000:8000 -v ${toubib_api_dir}/data:/data toubib:latest
