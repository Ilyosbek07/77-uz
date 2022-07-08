# Django start template

Django quick start template

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!


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
## Add your files
- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:
