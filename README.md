# DDS - Discord Bot

This is a Discord bot that can interact with people in a Discord Server.

## Commands

- !hallo
- !vliegavond
- !track
- !inspire

## Local Development

Follow the steps below to set up the project on your environment.
Create a virtual environment with Python 3.9 or higher.

Install required packages:

```bash
pip3 install -r requirements.txt
```

## Deployment

```bash
docker build -t dds-bot .
docker run -d dds-bot
```