import re

import openai
from decouple import config

openai.api_key = config("OPENAI_KEY")


class OpenAIApi:
    @staticmethod
    def completion_davinci_api(prompt: str):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt + '.\n"""Please Format your response in Markdown."""',
            temperature=0.3,
            max_tokens=1000,
            frequency_penalty=0.5,
            presence_penalty=0,
        )
        result = response.choices[0].text
        return result

    @staticmethod
    def chat_chatgpt_3_5(user_content, role_content="You are a helpful AI.") -> dict:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": role_content},
                {"role": "user", "content": user_content},
            ],
            temperature=0.4,
            max_tokens=1000,
        )
        result = response.choices[0].message
        return result

    @staticmethod
    def chat_chatgpt_3_5_data_insight(
        data_prompt,
        user_prompt,
        role_content="I am google analytics expert. you can ask me anything about the google analytics. if you provide me with the google analytics data or google analytics report data, i can provide you insights and recommendation based on the data. I can also provide the answer to the question based on the data. If you ask me the question out of context to data, i will respond with 'Inefficient Data'.",
    ) -> dict:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {
                    "role": "system",
                    "content": f"data:'''{role_content}'''. \nInstruction:Generated response should be in markdown format. The points should be in list. Key point and main point should be in bold.",
                },
                {"role": "user", "content": f"data:'''{data_prompt}'''"},
                {
                    "role": "user",
                    "content": f"{user_prompt}",
                },
            ],
            temperature=0.4,
            max_tokens=1000,
        )
        result = response.choices[0].message
        return result
