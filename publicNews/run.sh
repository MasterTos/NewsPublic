# python manage.py collectstatic
# python manage.py migrate
# python manage.py migrate --run-syncdb
# python manage.py runserver 0.0.0.0:8000

uwsgi --http :8000 --chdir /code -w publicNews.wsgi