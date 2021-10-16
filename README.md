# 🤖 DDS - Discord Bot

This is a Dutch Drone Squad - Discord bot, that can interact with people in a our Server.

## Commands

The bot responds to the commands below:

- `!hallo` - Just to say hello
- `!vliegavond` - Gives a link with information about our training days
- `!track` -  Gives information about the track
- `!inspire` - Inspiration quote

## Local Development

Follow the steps below to set up the project on your environment.

Create a virtual environment with Python 3.9 or higher and install the required packages:

```bash
pip3 install -r requirements.txt
```

## Deployment

```bash
docker build -t dds-bot .
docker run -d dds-bot
```

or

```bash
docker-compose up -d
```