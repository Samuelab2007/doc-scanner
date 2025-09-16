FROM python:3.13-trixie

RUN apt-get update && apt-get install -y --no-install-recommends libgl1 libglib2.0-0 tesseract-ocr tesseract-ocr-eng tesseract-ocr-spa tesseract-ocr-fra tesseract-ocr-deu tesseract-ocr-por tesseract-ocr-ita && rm -rf /var/lib/apt/lists/*
 

RUN pip install poetry==2.1.3

ENV POETRY_NO_INTERACTION=1 POETRY_VIRTUALENVS_IN_PROJECT=1 POETRY_VIRTUALENVS_CREATE=1 POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

# Install dependencies first
COPY pyproject.toml poetry.lock ./
RUN touch README.md
RUN poetry install --with api --no-root && rm -rf $POETRY_CACHE_DIR

COPY src/ ./src
COPY api/ ./api

RUN poetry install --with api

ENTRYPOINT ["poetry", "run", "fastapi", "run", "api/app.py"]
