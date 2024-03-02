"""Module to get a random quote from zenquotes.io."""

import json

import requests


def get_quote() -> str:
    """Get a random quote from zenquotes.io.

    Returns
    -------
        str: A random quote.

    """
    response = requests.get("https://zenquotes.io/api/random", timeout=10)
    json_data = json.loads(response.text)
    return json_data[0]["q"] + " - " + json_data[0]["a"]
