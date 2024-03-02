"""Cog to integrate with Twitch."""

import config
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands, tasks
from twitchAPI.twitch import Twitch as TwitchAPI
from twitchAPI.type import TwitchAPIException, TwitchAuthorizationException


class TwitchCog(commands.Cog, name="Twitch"):
    """Class to integrate with Twitch."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Twitch class."""
        self.bot = bot
        self.client_id = config.TWITCH_CLIENT_ID
        self.client_secret = config.TWITCH_CLIENT_SECRET
        self.twitch_api = TwitchAPI(self.client_id, self.client_secret)

        # List of Twitch channels to monitor
        self.channels = [
            "dutchdronesquad",
        ]
        self.notify_channel = config.TWITCH_CHANNEL_ID

        # Dictionary to store the live status and start time of each channel
        self.live_status = {
            channel: {"live": False, "start_time": None} for channel in self.channels
        }

    twitch = SlashCommandGroup(
        name="twitch", description="Commands specific about Twitch."
    )

    def cog_unload(self) -> None:
        """Cancel the background task."""
        self.stream_check.cancel()

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """Authenticate the Twitch API."""
        try:
            await self.twitch_api.authenticate_app([])
        except TwitchAuthorizationException:
            print("Failed to authenticate with Twitch.")
        else:
            print("Authenticated with Twitch.")
            # Initialize the live status of the channels
            await self.init_live_status()
            # Start the background task
            self.stream_check.start()

    @tasks.loop(minutes=5)
    async def stream_check(self) -> None:
        """Check if a Twitch user is live and notify in Discord."""
        for channel in self.channels:
            stream_found = False
            async for stream_info in self.twitch_api.get_streams(
                user_login=channel, stream_type="live"
            ):
                stream_found = True
                if stream_info.type == "live" and not self.live_status[channel]["live"]:
                    self.live_status[channel] = {
                        "live": True,
                        "start_time": stream_info.started_at,
                    }
                    await self.notify_live(stream_info)
            if not stream_found and self.live_status[channel]["live"]:
                self.live_status[channel] = {"live": False, "start_time": None}
        # print(self.live_status)

    @twitch.command(name="shoutout", description="Shoutout a Twitch user in the chat.")
    @discord.commands.option(name="username", description="The Twitch user to shoutout")
    async def twitch_shoutout(
        self,
        ctx: discord.ApplicationContext,
        username: str,
    ) -> None:
        """Shoutout a Twitch user in the chat.

        Args:
        ----
            ctx: The context in which the command was sent.
            user (str): The Twitch user to shoutout.

        """
        user_info = await self.get_user_info(login_name=username)
        if user_info:
            message = (
                f"📢 Ga naar https://twitch.tv/{user_info.login} "
                f"en volg {user_info.display_name}! 📢"
            )
            await ctx.respond(message)
        else:
            message = f"Geen Twitch gebruiker gevonden met de naam {username}."
            await ctx.respond(message, ephemeral=True)

    @twitch.command(
        name="streamers_monitor_list",
        description="Get the list of Twitch streamers to monitor.",
    )
    @commands.has_permissions(administrator=True)
    async def get_streamers_monitor_list(self, ctx: discord.ApplicationContext) -> None:
        """Get the list of Twitch streamers to monitor.

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        streamers_info = ""
        for channel, status in self.live_status.items():
            if status["live"]:
                start_time = status["start_time"].strftime("%Y-%m-%d %H:%M:%S")
                streamers_info += f"🟢 **{channel}**: Live since {start_time}\n"
            else:
                streamers_info += f"🔴 **{channel}**: Offline\n"
        embed = discord.Embed(
            title="Twitch Streamers Monitor List",
            description=streamers_info,
            color=discord.Colour.blurple(),
        )
        await ctx.respond(embed=embed)

    async def get_user_info(
        self,
        user_id: str | None = None,
        login_name: str | None = None,
    ) -> dict | None:
        """Get the user info of a Twitch user.

        Args:
        ----
            user_id (str): The user ID of the Twitch user.
            login_name (str): The login name of the Twitch user.

        Returns:
        -------
            dict: The user info of the Twitch user.

        """
        try:
            async for user in self.twitch_api.get_users(
                user_ids=user_id, logins=login_name
            ):
                # print(user.__dict__)
                return user
        except TwitchAPIException as error:
            print(f"Failed to get user info: {error}")
        else:
            return None

    async def notify_live(self, stream_info: dict) -> None:
        """Notify the server that a channel is live.

        Args:
        ----
            stream_info (dict): The information of the live stream.

        """
        # print(stream_info.__dict__)
        user_info = await self.get_user_info(user_id=stream_info.user_id)
        embed = self.create_embed(stream_info, user_info)

        channel = self.bot.get_channel(self.notify_channel)
        message = (
            f"Hey @everyone, {stream_info.user_name} is nu live op "
            f"https://twitch.tv/{stream_info.user_login}! Kom je ook kijken?"
        )
        await channel.send(message, embed=embed)

    def create_embed(self, stream_info: dict, user_info: dict) -> discord.Embed:
        """Create an embed for the live stream.

        Args:
        ----
            stream_info (dict): The information of the live stream.
            user_info (dict): The information of the Twitch user.

        Returns:
        -------
            discord.Embed: The embed for the live stream.

        """
        embed = discord.Embed(
            title=stream_info.title,
            url=f"https://twitch.tv/{stream_info.user_login}",
            description=user_info.description,
            color=discord.Colour.blurple(),
            timestamp=stream_info.started_at,
        )
        embed.add_field(name="Game", value=stream_info.game_name, inline=True)
        embed.add_field(name="Viewers", value=stream_info.viewer_count, inline=True)
        embed.set_image(url=stream_info.thumbnail_url.format(width=1920, height=1080))
        embed.set_footer(
            text="Twitch",
            icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Twitch_Glitch_Logo_Purple.svg/206px-Twitch_Glitch_Logo_Purple.svg.png",
        )
        return embed

    async def init_live_status(self) -> None:
        """Initialize the live status of the channels.

        Without this function, the bot will notify the server every time it starts
        """
        print("Initializing live status of Twitch streamers...")
        for channel in self.channels:
            async for stream_info in self.twitch_api.get_streams(
                user_login=channel, stream_type="live"
            ):
                if stream_info.type == "live":
                    self.live_status[channel] = {
                        "live": True,
                        "start_time": stream_info.started_at,
                    }
                    break
        # print(self.live_status)


def setup(bot: commands.Bot) -> None:
    """Add the Twitch cog to the bot."""
    bot.add_cog(TwitchCog(bot))
