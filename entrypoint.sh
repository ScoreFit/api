#!/bin/bash

echo "Environment: $ENVIRONMENT"

if [ "$ENVIRONMENT" = "dev" ]; then
    echo "Starting in development mode with reload..."
    exec uvicorn app.main:app --host $APP_HOST --port $APP_PORT --reload
else
    echo "Starting in production mode..."
    exec uvicorn app.main:app --host $APP_HOST --port $APP_PORT
fi
