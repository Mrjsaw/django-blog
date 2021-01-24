# Cyberbl0g

This is a blog created in Python Django Framework with a focus on security.

Take a look for yourself [Cyberbl0g](https://cyberbl0g.herokuapp.com/ "Cyberbl0g")

Visit the API page [Here](https://cyberbl0g.herokuapp.com/api/page "Cyberbl0g API")

Make a .env file inside of django-blog/djangoblog:

```

export SOCIAL_AUTH_AUTH0_DOMAIN = "<Auth0-Domain>"
export SOCIAL_AUTH_AUTH0_KEY = "<Auth0-Key>"
export SOCIAL_AUTH_AUTH0_SECRET = "<Auth0-Secret>" 
export YOUR_API_IDENTIFIER = "<Auth0-Public-Api>"

export DJANGO_SECRET_KEY = "<Django-Secret"
export DB_NAME = "<local-db-name>"
export DB_USER = "<local-db-user>"
export DB_PASSWORD = "<local-db-password>"


```

# Run Locally

First create a virtual environment

```python -m venv env```

On Windows

```./env/Scripts/activate```

Install python packages

```pip install -r requirements.txt```

Run server locally

```python manage.py runserver```

Migrate changes to postgreSQL (Make sure you are running a Server Locally)

```python manage.py makemigrations```

```python manage.py migrate```


# Deployment on Heroku + Auth0


Create an account on [Auth0](https://auth0.com/ "Auth0") and configure your .env

Set up a cloud hosting service for free on Heroku.

Download [HerokuCLI](https://devcenter.heroku.com/articles/heroku-cli "heroku-cli") add your app and push your repository to Heroku.

```heroku git:remote -a <your-heroku-git>```

```git push heroku master```

To update static folder

```heroku config:set DISABLE_COLLECTSTATIC=1```

```heroku python manage.py collectstatic```
