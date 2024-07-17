# syntax=docker/dockerfile:experimental
# Define global args
ARG RUNTIME_VERSION

FROM python:3.12-slim-bullseye as madewithpython

ENV APP_USER=it
ENV APP_USER_ID=1001
ENV APP_USER_HOME=/home/${APP_USER}
ENV APP_DIR=/server/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y curl gpg build-essential && \
    pip install -U pip setuptools wheel --no-cache-dir && \
    adduser \
    --system \
    --uid ${APP_USER_ID} \
    --home ${APP_USER_HOME} \
    --disabled-password \
    --group ${APP_USER}


RUN mkdir -p "${APP_DIR}"
WORKDIR ${APP_DIR}
RUN chown -R ${APP_USER}:${APP_USER} ${APP_DIR}
USER ${APP_USER}

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

ENV PATH="${APP_DIR}/.venv/bin:/home/${APP_USER}/.local/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    poetry config virtualenvs.prefer-active-python true && \
    poetry config virtualenvs.in-project true

FROM madewithpython

COPY --chown=${APP_USER}:${APP_USER} \
    poetry.lock \
    pyproject.toml \
    ./

COPY --chown=${APP_USER}:${APP_USER} web ./web

RUN uid=1001 poetry lock --no-update
RUN uid=1001 poetry install


EXPOSE 8000
CMD uvicorn web.main:app --host 0.0.0.0 --no-access-log --header server:madewithpython

