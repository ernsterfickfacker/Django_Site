
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
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/3fd462cd-697d-4d9b-8444-9d7030cb793e)

http://127.0.0.1:8000/swagger/ 
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/229667ba-5915-49d1-b525-fe964d8248df)
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/d522553f-a56d-442f-ae84-e67da4950778)

# Добавление на github
```
git add .
git commit -m 'commit message here'
git remote add origin https://github.com/ernsterfickfacker/Django_Site.git 
git branch -M main
git push -u origin main
```
