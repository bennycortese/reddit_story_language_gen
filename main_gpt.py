import os
import time

import modal

from modal import Image, Stub

bot_image = modal.Image.debian_slim().pip_install("openai")
bot_image = bot_image.pip_install("numpy")
bot_image = bot_image.pip_install("pandas")
bot_image = bot_image.pip_install("youtube_transcript_api")
bot_image = bot_image.pip_install("flask")
bot_image = bot_image.pip_install("flask_cors")

stub = modal.Stub("GPT wins 😔", image=bot_image)

@stub.function(secret=modal.Secret.from_name("my-openai-secret"))
def complete_text(prompt):
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a scene graph generator. You like taking in textual representations of an image and translating them into scene graphs."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message.content

@stub.function(secret=modal.Secret.from_name("my-anthropic-secret"))
def complete_text_anthropic(prompt):
    import anthropic

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=32000,
        temperature=0.0,
        system="Respond only in Yoda-speak.",
        messages=[
            {"role": "system", "content": "You are an instructor who is very good at grading."},
            {"role": "user", "content": prompt},
        ]
    )

    return message.content