# Cyberbl0g
This is a blog created in Python Django Framework with a focus on security.

Take a look for yourself [Cyberbl0g](https://cyberbl0g.herokuapp.com/ "Cyberbl0g")

Visit the API page [Here](https://cyberbl0g.herokuapp.com/api/page "Cyberbl0g API")

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

Download HerokuCLI and push this repository to your custom heroku .git

To update static folder:
```heroku config:set DISABLE_COLLECTSTATIC=1```

```heroku python manage.py collectstatic```
