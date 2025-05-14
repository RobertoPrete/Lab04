# To run this code you need to install the following dependencies:
# pip install google-genai

import base64
import os
from google import genai
from google.genai import types

# mNp1wc

def generate():
    client = genai.Client(
        api_key="AIzaSyAMpUk3qQsHxKJnJ7HC0nQaXqDW0",
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Input da controllare"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text="""Sei uno studente bravissimo a cui, fornendo un errore di un codice, fornisce il codice esatto ed una spiegazione. Tutti i commenti del codice dovranno essere in italiano"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
