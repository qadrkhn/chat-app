#!/bin/sh

echo "Applying the muigrations"

python manage.py migrate

exec "$@"
