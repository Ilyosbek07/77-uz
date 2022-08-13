# Django start template

Django quick start template

## ENVIRONMENT
#### Copy and Configure env with project settings
```
cp .env.example .env
cp config/settings/local_settings.example.py config/settings/local_settings.py
```

## SetUp with docker
#### ${PROJECT_NAME} is your project name
```
docker-compose -f docker-compose.yml -p ${PROJECT_NAME} build
docker-compose -f docker-compose.yml -p ${PROJECT_NAME} up
```

## SetUp without docker
```
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
