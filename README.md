## About

Production-ready Django + Django REST Framework boilerplate focused on fast API bootstrapping, predictable environment-based configuration, and container-first deployment.


## Features
- Environment-based settings (*development*, *stage*, *production*, *test*) according to the [Django Styleguide](https://github.com/HackSoftware/Django-Styleguide?tab=readme-ov-file#settings)
- Environment-based deployment using Docker Compose [profiles](https://docs.docker.com/reference/compose-file/profiles/)
- Integration with Nginx for reverse proxying and static file serving
- Integration with [uv](https://github.com/astral-sh/uv) for dependency management
- Integration with [ruff](https://github.com/astral-sh/ruff) and [mypy](https://github.com/python/mypy) for linting and type checking
- Integration with [django-debug-toolbar](https://github.com/django-commons/django-debug-toolbar), [django-silk](https://github.com/jazzband/django-silk) and [django-extensions](https://github.com/django-extensions/django-extensions) for smooth development experience
- Integration with [drf-spectacular](https://github.com/tfranzel/drf-spectacular) for OpenAPI schema generation and interactive API docs
- Integration with [django-unfold](https://github.com/unfoldadmin/django-unfold) for a modernized admin UI
- Basic CI pipeline using on Github Actions
- Basic logging configuration with console and file handlers
- Custom `User` model


### Future integrations
- Integration with PostgreSQL and Redis
- 


## Requirements

- Python: *>=3.12*
- Package/dependency manager: *uv*
- Container runtime (optional): Docker + Docker Compose


## Settings and configuration

Environment variables are loaded from the <ins>.env</ins> file that must be located in the root project directory.

You can generate it from the [.env.example](.env.example) and adjust values as needed:

```bash
cp .env.example .env
```


### Key variables

| Variable | Default | Description |
| --- | --- | --- |
| DJANGO_SETTINGS_MODULE | `main.django.development` | Active settings module |
| DJANGO_SECRET_KEY | generated at runtime if missing | Django secret key |
| DJANGO_DEBUG | `1` in example / `True` in base default | Debug mode toggle |
| DJANGO_ALLOWED_HOSTS | empty (plus localhost defaults) | Extra allowed hosts list |
| DATABASE_URL | `sqlite:///./db.sqlite3` (example) | Database connection URL |
| OPENAPI_TITLE | `Django APP` | OpenAPI title |
| OPENAPI_DESCRIPTION | `Django Boilerplate APP` | OpenAPI description |
| OPENAPI_VERSION | `0.0.1` | Exposed API version (`/version/`) |
| DJANGO_LOG_LEVEL | `INFO` | Global log level |
| DJANGO_LOG_FILEPATH | `./logs/app.log` | File log destination |
| UNFOLD_SITE_TITLE | `Django Admin Title` | Admin UI title |
| UNFOLD_SITE_HEADER | `Django Admin Header` | Admin UI header |
| BACKEND_HOSTNAME | `backend-dev` in example | Nginx upstream backend host |


**Note**: by default the application is running in the development mode. To switch to another environment, change the value of `DJANGO_SETTINGS_MODULE` accordingly (e.g. `main.django.production` for production mode).


## Installation
Step 1. clone the repository and navigate to the project directory:

```bash
git clone git@github.com:prathamlahoti123/Django-DRF-Boilerplate.git
cd Django-DRF-Boilerplate/
```

Step 2. install dependencies using *uv*:

```bash
uv sync --all-groups
```

Step 3. set up the configuration by creating a `.env` file and adjust values as needed:

```bash
cp .env.example .env
```

At this point you can run the application locally or using Docker Compose.


## Running
For running the application locally, you need to apply the database migrations, run the script to create a superuser, and then start the development server. For example:

```bash
uv run src/manage.py migrate
uv run src/manage.py createsuperuser
uv run src/manage.py runserver
```

Then Navigate to `http://localhost:8000` to access the application in your browser.

When using Docker Compose, everything will be provisioned and set up for you, so you can just run the appropriate command for the desired profile (see below) and access the app at `http://localhost`.

There are 3 profiles available:
- `dev` for development (with debug toolbar, silk profiler, etc.)
- `prod` for production-like environment
- `stage` for stage-like environment (same as prod but with different environment variables, e.g. `BACKEND_HOSTNAME`)

Example of running the application in production mode:

```bash
docker compose --profile prod up
```

If there's a need to build the backend service image (e.g. after making changes to the Dockerfile or the base image), you can do it with the following command:

```bash
docker compose build backend-prod
```


## Usage



## References

- [Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-spectacular](https://drf-spectacular.readthedocs.io/)
- [django-environ](https://django-environ.readthedocs.io/)
- [django-unfold](https://unfoldadmin.com/docs/)
- [Gunicorn](https://docs.gunicorn.org/)
- [uv](https://docs.astral.sh/uv/)
