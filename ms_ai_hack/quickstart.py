# -*- coding: utf-8 -*-
""" Azure OpenAI quickstart test """

import os
import time

import openai

# Azure portal - Keys & Endpoint section (you can use either KEY1 or KEY2).
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

# Azure OpenAI Studio > Playground > Code View (e.g.: https://docs-test-001.openai.azure.com/)
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")

# Azure Portal > Resource Management > Deployments or Azure OpenAI Studio > Management > Deployments
DEPLOYMENT_NAME = 'GPT35TEST'

openai.api_type = 'azure'

# this may change in the future
openai.api_version = '2023-05-15'


def main() -> None:
    """ Send a completion call to generate an answer """
    print('Sending a test completion job')
    start_phrase = 'Write a tagline for an ice cream shop.'
    start = time.time()
    response = openai.ChatCompletion.create(
        engine=DEPLOYMENT_NAME,
        max_tokens=50,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a tagline for an ice cream shop."},
            {"role": "assistant", "content": "\"Scoops of happiness in every cone!\""},
            {"role": "user", "content": "What is the name of the shop?"},
        ],
    )
    elapsed = time.time() - start
    text = response['choices'][0]['message']['content'].replace('\n', '').replace(' .', '.').strip()
    print(
        f"In: {start_phrase}\n\n"
        f"Out: {text}\n\n"
        f"Elapsed: {elapsed:.2f}s\n\n"
        f"Tokens used: {response['usage']['total_tokens']}\n\n"
        f"Response: {response}\n\n"
    )


if __name__ == '__main__':
    main()
