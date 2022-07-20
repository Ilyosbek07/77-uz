# Django start template

Django quick start template

## SetUp with docker
```
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```

## SetUp without docker
```
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
