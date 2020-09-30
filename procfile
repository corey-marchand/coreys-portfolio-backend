web: gunicorn portfolio_backend_project.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate