#!/usr/bin/env python3

import os
import openai
from dotenv import dotenv_values

env_variables = dotenv_values(".env")
openai.api_key = env_variables.get("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Ask me something",
  temperature=0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["\n"]
)