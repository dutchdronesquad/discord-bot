"""UI View for the role buttons."""

# ruff: noqa: ERA001
import discord

import config
from utils import custom_id

VIEW_NAME = "RoleView"


class RoleView(discord.ui.View):
    """RoleView class for handling role buttons."""

    def __init__(self) -> None:
        """Initialize the RoleView class."""
        super().__init__(timeout=None)

    async def handle_click(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle a button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        role_id = int(button.custom_id.split(":")[-1])
        role = interaction.guild.get_role(role_id)
        # assert isinstance(role, discord.Role)

        # If the user has the role
        if role in interaction.user.roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(
                f"Your {role.name} role has been removed.",
                ephemeral=True,
            )
        # If the user doesn't have the role
        else:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(
                f"You have been given the {role.name} role.",
                ephemeral=True,
            )

    @discord.ui.button(
        label="Rookie",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.ROOKIE_ROLE_ID),
    )
    async def rookie_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the rookie button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)

    @discord.ui.button(
        label="Advanced",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.ADVANCED_ROLE_ID),
    )
    async def advanced_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the advanced button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)

    @discord.ui.button(
        label="Analog",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.ANALOG_ROLE_ID),
    )
    async def analog_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the analog button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)

    @discord.ui.button(
        label="Digital",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.DIGITAL_ROLE_ID),
    )
    async def digital_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the digital button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)

    @discord.ui.button(
        label="Racing",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.RACING_ROLE_ID),
    )
    async def racing_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the racing button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)

    @discord.ui.button(
        label="Freestyle",
        style=discord.ButtonStyle.primary,
        custom_id=custom_id(VIEW_NAME, config.FREESTYLE_ROLE_ID),
    )
    async def freestyle_button(
        self,
        button: discord.ui.Button,
        interaction: discord.Interaction,
    ) -> None:
        """Handle the freestyle button click.

        Args:
        ----
            button (discord.ui.Button): The button that was clicked.
            interaction (discord.Interaction): The interaction that was made.

        """
        await self.handle_click(button, interaction)
