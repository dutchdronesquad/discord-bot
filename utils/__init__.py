"""The utility functions for the bot."""
import config


def custom_id(view: str, button_id: int) -> str:
    """Return the view with the ID.

    Args:
    ----
        view (str): The view name.
        button_id (int): The ID of the button.

    Returns:
    -------
        str: The custom ID.

    """
    return f"{config.BOT_NAME}:{view}:{button_id}"
