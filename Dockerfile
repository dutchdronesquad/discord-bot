FROM python:3.10-slim
LABEL Maintainer="Klaas Schoute"

WORKDIR /usr/src/bot

# copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

ENTRYPOINT ["python"]
CMD ["main.py"]