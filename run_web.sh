#!/bin/bash
# set -e : forces script to exit if something goes wrong
set -e

cd users_posts

# run this for generating a .env file the official SECRET_KEY is only in production
python env_generator.py

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
