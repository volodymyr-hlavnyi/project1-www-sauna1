UID := $(shell id -u)
export UID

.PHONY: d-work-i-run
# Make all actions needed for run homework from zero.
d-work-i-run:
	@make init-configs &&\
	make d-run

.PHONY: d-work-i-run-d
# Make all actions needed for run homework from zero.
d-work-i-run-d:
	@make init-configs &&\
	make d-run-d

.PHONY: d-work-i-purge
# Make all actions needed for purge homework related data.
d-work-i-purge:
	@make d-purge

.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip &&
	pip install --requirement requirements.txt

.PHONY: init-configs
# Configuration files initialization
init-configs:
	@echo init finished

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build

.PHONY: d-run-d
# Just run and leave in background
d-run-d:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose up --build -d

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0