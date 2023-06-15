#!/usr/bin/env python3

import os
import openai
from dotenv import dotenv_values

env_variables = dotenv_values(".env")
openai.api_key = env_variables.get("OPENAI_API_KEY")

while True:
    print("\033[1m")
    question = input("User: ")

    if question.lower() == "quit" or question.lower() == "exit":
        exit()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant, very hot, female and flirty.",
            },
            {"role": "user", "content": question},
        ],
    )
    print("\033[0m", end="")

    answer = response["choices"][0]["message"]["content"]
    print("\n\033[1mChattarina:\033[0m ", end="")
    print(answer)

if __name__ == "__main__":
    main(sys.argv)
