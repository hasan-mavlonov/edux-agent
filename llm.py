import os
import requests
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "qwen/qwen3.6-flash"  # change here, nowhere else


def call_model(messages, tools=None):
    """Send the full message list to the model, return the assistant message."""
    payload = {"model": MODEL, "messages": messages}
    if tools:
        payload["tools"] = tools  # unused until tools.py exists

    response = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"},
        json=payload,
        timeout=60,  # never wait forever
    )
    response.raise_for_status()  # crash loudly on 4xx/5xx instead of hiding it
    data = response.json()

    # the whole message object, not just text: Wednesday's loop needs its other fields
    return data["choices"][0]["message"]