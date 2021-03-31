NO_COLOUR=\033[0m
OK_COLOUR=\033[32m
INFO_COLOUR=\033[33m
ERROR_COLOUR=\033[31;01m
WARN_COLOUR=\033[33;01m


# Containers ids
ID-API=$(shell docker ps -a -q -f "name=pokemon-api")
ID-POSTGRES=$(shell docker ps -a -q -f "name=pokemon-postgres")
ID-REDIS=$(shell docker ps -a -q -f "name=pokemon-redis")


black:  # run the black formatter
	@docker exec -t pokemon-api black $(ARGS) ./ --exclude /migrations/

isort: # run isort
	@docker exec -t pokemon-api isort $(ARGS) ./

format: black isort


# Build all containers
build-all: build-api build-postgres build-redis

build-api:
	@docker-compose -f docker-compose.yml build pokemon-api
build-postgres:
	@docker-compose -f docker-compose.yml build pokemon-postgres
build-redis:
	@docker-compose -f docker-compose.yml build pokemon-redis


# run all containers
run-all:
	@docker-compose -f docker-compose.yml up

# run services without fastapi server
run-services:
	@docker-compose -f docker-compose.yml up pokemon-postgres pokemon-redis

# run fastapi server
run-api:
	@docker-compose -f docker-compose.yml up pokemon-api

# attach shell to runing server container
shell-api:
	@docker exec -it $(ID-API) bash

# Stop docker containers
stop-all: stop-api stop-postgres stop-redis
stop-api:
	@docker stop $(ID-API)
stop-postgres:
	@docker stop $(ID-POSTGRES)
stop-redis:
	@docker stop $(ID-REDIS)


# Remove docker containers
rm-all: rm-api rm-postgres rm-redis
rm-api:
	@docker rm --volumes $(ID-API)
rm-postgres:
	@docker rm --volumes $(ID-POSTGRES)
rm-redis:
	@docker rm --volumes $(ID-REDIS)

# Rebuild docker containers - stop -> remove -> build
rebuild-all: clean-all build-all
rebuild-api: clean-api build-api
rebuild-postgres: clean-postgres build-postgres
rebuild-redis: clean-redis build-redis

# Clean docker containers
clean-all: clean-api clean-postgres clean-redis
clean-api: stop-api rm-api
clean-postgres: stop-postgres rm-postgres
clean-redis: stop-redis rm-redis

# populate db with pokemon data
populate-db:
	@docker exec $(ID-API) poetry run python src/utils/create_pokemon_db.py
