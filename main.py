"""Main file to start the bot."""
import os

import discord
from discord.ext import commands

import config


def main() -> None:
    """First function to run when starting the bot."""
    intents = discord.Intents.default()
    intents.guilds = True
    intents.message_content = True

    activity = discord.Activity(
        type=discord.ActivityType.watching, name="de DDS server"
    )

    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or(config.PREFIX),
        intents=intents,
        activity=activity,
        owner_id=config.OWNER_ID,
    )
    loaded: list = []

    # List of folders to ignore
    folders_to_ignore = ["__pycache__"]

    # Load all modules (cogs)
    for folder in os.listdir("modules"):
        if folder not in folders_to_ignore:
            try:
                bot.load_extension(f"modules.{folder}")
                loaded.append(folder)
            except Exception as error:  # noqa: BLE001
                print(f"Failed to load module {folder}: {error}")

    # Print all loaded modules
    loaded_str: str = ", ".join(loaded)
    print(f"Successfully loaded modules (cogs): {loaded_str}")

    # Run the bot
    bot.run(config.BOT_TOKEN)


# Run main() to start the bot
if __name__ == "__main__":
    main()
