release: python manage.py migrate
web: gunicorn qurritv_3.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate