# Запуск 
```
python -m venv venv
venv\Scripts\activate
cd kanban-main
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Starting development server at http://127.0.0.1:8000/

# Добавление на github
```
git add .
git commit -m 'commit message here'
git remote add origin https://github.com/ernsterfickfacker/Django_Site.git 
git branch -M main
git push -u origin main
```
