FROM python:3.11-slim
LABEL Maintainer="Klaas Schoute"

COPY . /usr/src/bot
WORKDIR /usr/src/bot

# Install poetry and dependencies
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --without dev

ENTRYPOINT ["python"]
CMD ["main.py"]