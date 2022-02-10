# DjangoFoodie ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## A full stack Django Application for Food Delivery

> Some Django Commands to be run on PowerShell

| Command | Description |
|---------|-------------|
| `pip install virtualenv`| It installs virtual environment|
| `virtualenv env` | It creates an environment named `env`|
| `.\env\Scripts\activate.ps1` | It activates the environment|
| `deactivate` | It deactivates the environment|
| `django-admin startproject <projectname>`| It creates the Django Project|
| `python manage.py startapp <appname>`| It creates the app. Make sure to create `urls.py` in your app and install it in `settings.py`|
| `python manage.py runserver`| It starts the development server|
| `python manage.py collectstatic`| It collect all the static files(img, css, js) to the server|
| `python manage.py makemigrations`| It prepares the models.py for DB migrations|
| `python manage.py migrate`| It migrates the data to the DB|
| `python manage.py createsuperuser`| It creates the admin of admin page|

---

For the module that we have to install, refer to **[requirements.txt](https://github.com/pranavarora1895/DjangoFoodie/blob/main/requirements.txt)**

> To get this project in your PC, follow these steps:-

* Clone this project
* Make an environment
* Activate the environment
* Add this command - `pip install -r requirements.txt`

