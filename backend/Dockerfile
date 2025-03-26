FROM python:3.13-slim as requirements-stage

WORKDIR /tmp

#
RUN pip install poetry
RUN pip install poetry-plugin-export

COPY pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM requirements-stage

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY app /code/app
COPY alembic.ini /code/
COPY scripts /code/scripts

CMD uvicorn app.main:app --host=0.0.0.0 --port=80