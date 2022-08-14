from dotenv import load_dotenv
from random import choice
import os
import openai
import requests


class gpt3_prompt():
    load_dotenv()
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    

    def get_question(self, user_prompt):
        # print(question_type)
        # if(question_type == "age"):
        #     user_prompt = "He is only 15 years old"
        # elif(question_type== "color"):
        #     user_prompt = "I like blue"
        # elif(question_type == "gender"):
        #     user_prompt = "I'm a male"
        # elif(question_type == "size"):
        #     user_prompt = "I wear M size"
        # elif(question_type == "clothing_pref"):
        #     user_prompt = "I want to buy jeans"
        response = openai.Completion.create(
            model="davinci:ft-personal-2022-06-17-20-02-44",
            prompt=user_prompt)

        text = response['choices'][0]['text']
        processed_text = text.split('\n')
        processed_text = processed_text[0].split('->')
        print(type(processed_text[1]))
        return processed_text[1]
