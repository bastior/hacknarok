rm db.sqlite3
python manage.py migrate
python manage.py loaddata hackathon/fixtures/dump.json
python manage.py runserver
