#!/bin/bash
echo "Running from entrypoint.sh"

# Run all migrations
python3 src/manage.py migrate

# Collect static files
python3 src/manage.py collectstatic --noinput

# Create superuser
python3 src/manage.py create_superuser

# Start the server
python3 src/main.py
