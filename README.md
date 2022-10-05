# 🤖 DDS - Discord Bot

This is a [Dutch Drone Squad][dds] - Discord bot, that can interact with people in a our server.

## Installation

Would you like to use the bot on your own server? Then click on the installation button below to start the wizard for adding to a server.

[![Discord][bot-label]][bot-link]

## Commands

The bot responds to the commands below:

- `!hallo` - Just to say hello
- `!vliegavond` - Gives a link with information about our training days
- `!track` -  Gives information about the track
- `!inspire` - Inspiration quote
- `!version` - Shows the version of the bot (admin only)

## Local Development

It's advisable to test the bot during development in a separate server and use
a separate token for a production or development. In this project it was
decided to make a `production.yaml` for production stack deploy and
`docker-compose.yml` for development.

Follow the steps below to set up the project on your environment.

<details>
  <summary>Click to expand!</summary>

### Setup your environment

Create a virtual environment with Python 3.9 or higher and install the required packages:

```bash
pip3 install -r requirements.txt
```

Create an `.env` file and enter your **BOT_DEV_TOKEN**.

```bash
cp .env.example .env
```

If you set **TESTING** to `true` the development token is used.

### Run the application

To run it on your development setup, you can either run the python file (main.py), run it as single docker container by building and running the container or by using docker-compose.

#### Python

The simplest is to run the python file directly with:

```bash
python3 main.py
```

#### single docker container

start the docker container and give it your Discord Developers bot token.

```bash
docker build -t dds-bot-dev .
docker run --name DDS-Bot-Dev -d -e TOKEN="[YOUR TOKEN]" dds-bot-dev
```
or if you use want to test the latest docker image from the Github container registry.

```bash
docker pull ghcr.io/dutchdronesquad/dds-bot:latest
docker run --name DDS-Bot -d -e TOKEN="[YOUR TOKEN]" dds-bot:latest
```

#### docker-compose

Use docker compose to build and run the container:

```bash
docker-compose up -d --build
```
</details>

[dds]: https://dutchdronesquad.nl
[bot-label]: https://img.shields.io/badge/DDS--Bot-Invite-orange?style=for-the-badge&logo=robotframework
[bot-link]: https://discord.com/api/oauth2/authorize?client_id=897994664316133386&permissions=448824428608&scope=bot%20applications.commands