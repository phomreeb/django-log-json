# Project Overview

This is a Django demonstration project designed to showcase JSON logging patterns. It is configured to output structured JSON logs using the `python-json-logger` package, which is beneficial for integration with log aggregation and monitoring systems (e.g., ELK stack, Datadog). 

**Key Technologies:**
- **Python:** >= 3.13
- **Framework:** Django (>= 6.0.5)
- **API:** Django REST Framework (included in dependencies)
- **Logging:** `python-json-logger`
- **Dependency Management:** `uv`

**Architecture Highlights:**
- The main project configuration is stored in the `config/` directory.
- Logging configuration is cleanly separated into its own module at `config/logger/log_settings.py` and imported into the main `settings.py`.
- Log files (`django.log` and `django_error.log`) are generated and rotated automatically inside a `logs/` directory at the project root.

# Building and Running

This project uses `uv` for fast dependency management. Ensure you have `uv` installed.

**Install Dependencies:**
```bash
uv sync
```

**Database Migrations:**
```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

**Run the Development Server:**
```bash
uv run python manage.py runserver
```

**Run Tests:**
*(No custom tests discovered yet, but standard Django testing applies)*
```bash
uv run python manage.py test
```

# Development Conventions

- **Logging Separation:** Any updates to logging logic should be made in `config/other_settings/logger.py` rather than cluttering the main `settings.py`.
- **JSON Structured Logs:** Standard output (`console`) uses a verbose string format, but file handlers output exclusively in JSON to `logs/django.log` and `logs/django_error.log`. Maintain this pattern for production readiness.
- **Dependency Management:** Use `uv add <package>` to manage dependencies, which will automatically update `pyproject.toml` and `uv.lock`.