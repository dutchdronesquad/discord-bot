import discord
import os
import config

from discord.ext import commands

def main():
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

    # Load all modules (cogs)
    for module in os.listdir('modules'):
        try:
            bot.load_extension(f'modules.{module}')
            loaded.append(module)
        except Exception as error:
            print(f'Failed to load module {module}: {error}')

    # Print all loaded modules
    loaded = ', '.join(loaded)
    print(f'Successfully loaded modules (cogs): {loaded}')

    # Run the bot
    bot.run(config.BOT_TOKEN)

# Run main() to start the bot
if __name__ == "__main__":
    main()