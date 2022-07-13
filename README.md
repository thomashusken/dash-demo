# dash-demo
Simple Dash app to try out the Objectiv tracker

## How to run

### Python

[**Poetry**](https://python-poetry.org/) is used to manage dependencies and virtual environments. Please
follow the installation instructions fir Poetry for your respective OS. The dependencies
can then be installed by:

- `poetry install`

To run the app locally, use:

- `poetry python run app.py`

This will run the app on `localhost:8000/gapminder`.

### Docker

Alternatively, you can run the app as a docker container:

- `docker build . -t dash-demo:latest`
- `docker run -d -p 8000:8000`
