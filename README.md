# 🤖 DDS - Discord Bot

This is a [Dutch Drone Squad][dds] - Discord bot, that can interact with
people in a our server.

## Features

The bot responds to the `!` commands below:

- `!hallo` - Just to say hello
- `!track` -  Gives information about the track
- `!inspire` - Inspiration quote

Or slash commands like:

- `/race training` - Gives a link with information about our training days
- `/race track` - Gives information about the track
- `/race results` - Gives a link where you can find the results of training

### Twitch Integration

The bot also has a Twitch integration, where it will post a message in
a specific channel when DutchDroneSquad goes live. It needs a Twitch API
client ID and secret to work.

- `/twitch shoutout` - Gives a shoutout to a streamer

### Owner Commands

- `!version` - Shows the version of the bot
- `!roles` - Gives the option to add or remove roles for users

## Setting up development environment

It's advisable to test the bot during development in a separate server and use
a separate token for a production or development. In this project it was
decided to make a `production.yaml` for production stack deploy and
`docker-compose.yml` for development.

Follow the steps below to set up the project on your environment.

<details>
  <summary>Click to expand!</summary>

### Install dependencies

This Python project relies on [Poetry][poetry] as its dependency manager,
providing comprehensive management and control over project dependencies.

You need at least:

- Python 3.11+
- [Poetry][poetry-install]

Install all packages, including all development requirements:

```bash
poetry install
```

Poetry creates by default an virtual environment where it installs all
necessary pip packages, to enter or exit the venv run the following commands:

```bash
poetry shell
exit
```

Create an `.env` file and enter the missing details (token from
[developers portal][dev-portal] and ID's).

```bash
cp .env.example .env
```

### Run the application

To run it on your development setup, you can either run the python file
(main.py), run it as single docker container by building and running the
container with docker compose.

#### Python

The simplest is to run the python file directly with:

```bash
python main.py
```

#### docker-compose

Use docker compose to build and run the container:

```bash
docker-compose up -d --build
```
</details>

<!-- Links -->
[dds]: https://dutchdronesquad.nl

<!-- Development Links -->
[dev-portal]: https://discord.com/developers/applications
[poetry-install]: https://python-poetry.org/docs/#installation
[poetry]: https://python-poetry.org