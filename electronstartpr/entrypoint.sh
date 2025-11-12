#!/bin/sh

if [ "$POSTGRES_DB" = "db_electron" ]
then
    echo "Загрузка postgres..."

    while ! nc -z "db" $POSTGRES_PORT; do
        sleep 0.5
    done

    echo "Postgres запущен"
fi

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"