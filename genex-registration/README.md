#  How to run this projects ?

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

