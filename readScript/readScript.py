from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()


def getFile(dir="newsFiles/script/script.txt"):
    with open(dir, "r") as file:
        content = file.read()
    return content


def readScript():
    content = getFile()
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=content,
        instructions="Formal tone, and add emotion when necessary.",
    ) as response:
        response.stream_to_file(speech_file_path)
