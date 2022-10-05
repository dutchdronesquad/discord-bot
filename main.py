import discord
import os
import config

from discord.ext import commands

def main():
    intents = discord.Intents.default()
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

    @bot.event
    async def on_ready():
        print("--- Bot is online and ready to interact! ---")
        print(f'{bot.user.name} has connected to Discord (ID: {bot.user.id})')

    @bot.event
    async def on_message(message: discord.Message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username} in #{channel}: {user_message}')

        if message.author == bot.user:
            return

        # msg = message.content

        # if any(word in msg for word in sad_words):
        #     await message.reply(random.choice(happy_response))

        # Leave this here, otherwise commands wil stop running
        await bot.process_commands(message)

    # Load all modules
    for folder in os.listdir('modules'):
        bot.load_extension(f'modules.{folder}')

    # Run the bot
    if config.TESTING == "true":
        bot.run(config.BOT_DEV_TOKEN)
    else:
        bot.run(config.BOT_TOKEN)

# Run the bot
if __name__ == "__main__":
    main()