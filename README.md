# 🤖 DDS - Discord Bot

This is a [Dutch Drone Squad][dds] - Discord bot, that can interact with people in a our server.

## Commands

The bot responds to the commands below:

- `!hallo` - Just to say hello
- `!vliegavond` - Gives a link with information about our training days
- `!track` -  Gives information about the track
- `!inspire` - Inspiration quote

## Run the application

First you need to pull the image from the Github container registry.

```bash
docker pull ghcr.io/dutchdronesquad/dds-bot:latest
```

Then start the docker container and give it your Discord Developers bot token.

```bash
docker run --name DDS-Bot -d -e TOKEN="[YOUR TOKEN]" dds-bot:latest
```

## Local Development

Follow the steps below to set up the project on your environment.

<details>
  <summary>Click to expand!</summary>

Create a virtual environment with Python 3.9 or higher and install the required packages:

```bash
pip3 install -r requirements.txt
```

### Run it

To run it on your development setup, you can either run it as single docker container by building and running the container.

```bash
docker build -t dds-bot-dev .
docker run --name DDS-Bot-Dev -d -e TOKEN="[YOUR TOKEN]" dds-bot-dev
```

or with the help of docker-compose:

```bash
docker-compose up -d
```

</details>

[dds]: https://dutchdronesquad.nl