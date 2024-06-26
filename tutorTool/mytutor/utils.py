import os
from openai import OpenAI


def get_gpt_response(prompt):
    client = OpenAI(
        api_key = "<your_key_here>",
    )

    response = client.chat.completions.create(
      model = "gpt-3.5-turbo",
      messages = [
        {"role": "system", "content": "You are a helpful study assistant."},
        {"role": "user", "content": prompt},
      ]
    )

    return response.choices[0].message.content.strip()