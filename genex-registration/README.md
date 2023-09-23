#  How to run this projects ?
The Django Custom User Registrations and Login project aims to provide a customizable user registration and login system using Django, a popular Python web framework. The project provides a foundation for building user authentication functionality tailored to your specific needs.

# clone github repo.

```bash
git clone  # repo link
```
### Create virtual env 
```bash
python -m venv env

# activate venv 
sources env/Scripts/activate
```
#### install reqierments:
```bash
pip install -r reqierments.txt
```
#### create database 
```mysql
CREATE DATABASE genex_db;
```

#### setup django setting.py file database 
/
update mysql password and user name
/

after that

#### migrate and migrations

```bash
python manage.py makemirations
python manage.py migrate
```

#### run cmd 

```bash
python manage.py runserver
```

