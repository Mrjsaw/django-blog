# django-blog
This is a blog created in Python Django Framework with a focus on security.

# Run Locally

First create a virtual environment

```python -m venv env```

On Windows:

```./env/Scripts/activate```

Install python packages:

```pip install -r requirements.txt```

Run server locally

```python manage.py runserver```


# Deployment on Heroku:

To update static folder:
```heroku config:set DISABLE_COLLECTSTATIC=1```
```heroku python manage.py collectstatic```
