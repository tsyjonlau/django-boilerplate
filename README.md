# django-react-boilerplate

A boilerplate for developing web applications using Django and React.

## Setup back-end

#### Install python
https://www.python.org/downloads/
After installation, add python executable directory to PATH.

#### Create a virtual environment
https://docs.python.org/3/library/venv.html

#### (Bonus step) Upgrade pip and setuptools
```
pip install -U pip setuptools
```

#### Install python packages with Poetry
Note that the current poetry.toml prevents Poetry to create a new environment when installing packages.
```
pip install poetry
cd src
poetry config virtualenvs.create false --local
poetry install
```

#### Generate new migrations
```
# in /src folder
python manage.py makemigrations
```

#### Migrate database
```
# in /src folder
python manage.py migrate
```

#### Run web server in development
Note that this runs on http://localhost:8000.
```
# in /src folder
python manage.py runserver
```

#### Create superuser for admin website
```
python manage.py createsuperuser
```

## Setup front-end

#### Install node.js
https://nodejs.org
After installation, add node executable directory to PATH.

#### (Bonus step) Upgrade npm
```
npm i -g npm
```

#### Install JS dependencies with Yarn
```
npm i -g yarn
cd src/frontend
yarn
```

#### Run dedicated web server for serving front-end in development mode
Note that this runs on http://localhost:3000.
For production we will serve front-end from the same domain. Refer to next section.
```
# in /src/frontend folder
yarn start
```

## Setup for production

#### Build front-end for production
```
# in /src/frontend folder
yarn build
```

#### Generate static files
Note that the `staticfiles` folder has to be created in order to be able retrieve all static files.
This collects all static files specified in the `STATICFILES_DIRS` setting.
```
python manage.py collectstatic
```

#### Run web server in production
```
python manage.py runserver --nostatic
```