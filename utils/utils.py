import config

def custom_id(view: str, id: int) -> str:
    """Return the view with the ID"""
    return f"{config.BOT_NAME}:{view}:{id}"