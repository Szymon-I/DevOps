#!/usr/bin/env bash
set -ex

poetry run python ./scripts/wait_redis_postgres.py
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000