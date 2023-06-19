# -*- coding: utf-8 -*-
""" Azure OpenAI quickstart test """

import os

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
    start_phrase = 'Write a tagline for an ice cream shop. '
    response = openai.Completion.create(engine=DEPLOYMENT_NAME, prompt=start_phrase, max_tokens=10)
    text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
    print(start_phrase+text)


if __name__ == '__main__':
    main()
