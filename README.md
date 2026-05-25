# Django JSON Logging Demo

This is a Django demonstration project designed to showcase structured JSON logging patterns. It is configured to output JSON logs using the `python-json-logger` package, which is ideal for integration with log aggregation and monitoring systems like the ELK stack, Datadog, or Splunk.

## Features

- **Python & Django:** Built with Python 3.13+ and Django 6.0+.
- **Structured Logging:** Utilizes `python-json-logger` for JSON-formatted file logs.
- **Separation of Concerns:** Logging configuration is cleanly separated into its own module (`config/other_settings/logger.py`) to keep the main `settings.py` clean.
- **Log Rotation:** Log files (`django.log` and `django_error.log`) are generated and rotated automatically inside the `logs/` directory.
- **Dependency Management:** Fast and reliable dependency management using `uv`.

## Prerequisites

- [Python](https://www.python.org/) >= 3.13
- [uv](https://github.com/astral-sh/uv) (for dependency management)

## Getting Started

### 1. Install Dependencies

Use `uv` to sync and install the project dependencies:

```bash
uv sync
```

### 2. Run Database Migrations

Apply the default Django migrations:

```bash
uv run python manage.py migrate
```

### 3. Run the Development Server

Start the local development server:

```bash
uv run python manage.py runserver
```

You can now access the project at `http://127.0.0.1:8000/`.

## Logging Details

- **Console Output:** Development-friendly verbose string formatting.
- **File Output:** Production-ready structured JSON logs.
  - Standard logs: `logs/django.log`
  - Error logs: `logs/django_error.log`

To update or modify the logging behavior, edit `config/other_settings/logger.py`.

## Testing

Run the standard Django test suite using:

```bash
uv run python manage.py test
```
