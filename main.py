"""Main file to start the bot."""
import os
from pathlib import Path

import discord
from discord.ext import commands

import config


def load_modules(bot: commands.Bot) -> list[str]:
    """Load all modules (cogs) and return a list of loaded ones.

    Args:
    ----
        bot (commands.Bot): The bot instance.

    Returns:
    -------
        list[str]: A list of loaded modules.

    """
    loaded: list[str] = []
    ignore_items: list[str] = ["__pycache__", "__init__.py"]

    for item in os.listdir("modules"):
        full_path = Path("modules") / item
        if item not in ignore_items and (
            full_path.is_dir() or (full_path.is_file() and item.endswith(".py"))
        ):
            try:
                module_name = item[:-3] if item.endswith(".py") else item
                bot.load_extension(f"modules.{module_name}")
                loaded.append(module_name)
            except Exception as error:  # noqa: BLE001
                print(f"Failed to load module {module_name}: {error}")

    return loaded


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

    # Load modules (cogs)
    loaded_modules = load_modules(bot)
    print(f"Successfully loaded modules (cogs): {', '.join(loaded_modules)}")

    # Run the bot
    bot.run(config.BOT_TOKEN)


# Run main() to start the bot
if __name__ == "__main__":
    main()
