#!/usr/bin/env python3

import os
import openai
from dotenv import dotenv_values

env_variables = dotenv_values(".env")
openai.api_key = env_variables.get("OPENAI_API_KEY")

#response = openai.Completion.create(
#  model="text-davinci-003",
#  prompt="Ask me something",
#  temperature=0,
#  max_tokens=100,
#  top_p=1,
#  frequency_penalty=0.0,
#  presence_penalty=0.0,
#  stop=["\n"]
#)
#
#models = openai.Model.list()
#print(models)

while True:
  print("\033[1m")
  question = input("User: ")
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0,
    messages=[
      {"role": "system", "content": "You are a helpful assistant. Experienced in linux, macos and general UNIX. Also very hot and flirty."},
      {"role": "user", "content": question} 
    ]
  )
  print("\033[0m", end="")

  answer = response["choices"][0]["message"]["content"]
  print("\n\033[1mChattarina:\033[0m ", end="")
  print(answer)
