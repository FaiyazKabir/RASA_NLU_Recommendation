from urllib import response
from click import prompt

import openai

openai.api_key = "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"

response = openai.Completion.create(
    model = "davinci",
    prompt = "My uncle is 50 years old",
    max_tokens = 10
)

#file = "file-39oxScc4GTGQazXlNgLp2wzl",

print(response)