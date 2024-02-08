#!/bin/bash

perform_migration() {
    alembic upgrade head
    return $?
}

if perform_migration; then
    echo "Alembic migration successful. Starting FastAPI application."
    # Start FastAPI application
    uvicorn app.main:app --host 0.0.0.0 --port 8000
else
    echo "Error: Alembic migration failed. FastAPI application will not start."
    exit 1
fi
