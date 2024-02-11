
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
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/fbebbab3-e304-48ed-b624-052b1d3d2e28)
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/3fd462cd-697d-4d9b-8444-9d7030cb793e)

http://127.0.0.1:8000/swagger/ 
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/229667ba-5915-49d1-b525-fe964d8248df)
![image](https://github.com/ernsterfickfacker/Django_Site/assets/93219479/1a1c7d3f-eb7c-4b72-b862-5d9525618407)


# Добавление на github
```
git add .
git commit -m 'commit message here'
git remote add origin https://github.com/ernsterfickfacker/Django_Site.git 
git branch -M main
git push -u origin main
```
