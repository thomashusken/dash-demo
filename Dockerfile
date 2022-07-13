FROM python:3.8-slim-buster

RUN apt-get update; apt-get install curl -y

WORKDIR /var/task

ENV FLASK_APP=app:app

COPY . ./

# Poetry will be installed here
ENV POETRY_HOME=/poetry

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Looks like poetry fails to add itself to the Path in Docker. We add it here.
ENV PATH="/poetry/bin:${PATH}"

# Install requirements via Poetry, disable venv creation since we're already in a Docker container
RUN POETRY_VIRTUALENVS_CREATE=false poetry install -vvv --no-ansi --no-dev

CMD ["gunicorn", "app:server", "-b", "0.0.0.0:8000", "-w", "3"]
