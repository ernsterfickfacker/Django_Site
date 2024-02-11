python -m venv venv
venv\Scripts\activate

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
