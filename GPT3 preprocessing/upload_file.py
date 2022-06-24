import os
import openai
import wandb

openai.api_key = "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"


response = openai.File.create(
    file=open("Q_A_survey_prepared.jsonl"),
        purpose='fine-tune'
    )

print(response)