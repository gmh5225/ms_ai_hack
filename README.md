:b: ms_openai_hack
=============

Our main goals for this event are to familiarize ourselves with the Azure AI tools and gain more knowledge about the various tools available and how to effectively utilize them.

Throughout the hackathon, we aim to explore and understand the different tools offered by Azure AI. By immersing ourselves in these tools, we will not only expand our technical capabilities but also develop a deeper understanding of their functionalities, features, and potential applications.


Theme
----------
* [OpenAI Hackathon Event](https://msevents.microsoft.com/event?id=3230355812)
* [Introduction to Azure OpenAI Service](https://learn.microsoft.com/en-us/training/modules/explore-azure-openai/)
* [Develop AI solutions with Azure OpenAI](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/)
* [Hackathon Starter Kit](https://github.com/microsoft/hackathon-starter-kit/)
* [Getting started with generative AI using Azure OpenAI Service](https://build.microsoft.com/en-US/sessions/27c0f55d-9c02-4003-bfb3-7e077a12fea2?source=sessions)


Resources
----------
* Access to Azure OpenAI (corporate access)
* Azure subscription/Azure Pass
* Rights to deploy new resources

Key & Endpoint
----------
To successfully make a call against the Azure OpenAI service, you'll need the following:
* [ENDPOINT](https://portal.azure.com/?microsoft_azure_marketplace_ItemHideKey=microsoft_openai_tip#@bitdefender.onmicrosoft.com/resource/subscriptions/7902f377-3b93-4897-a40d-4d2ea573325f/resourceGroups/ms-openai-hackathon/providers/Microsoft.CognitiveServices/accounts/MS-OpenAI-Hackathon/cskeys)
* [API-KEY](https://portal.azure.com/?microsoft_azure_marketplace_ItemHideKey=microsoft_openai_tip#@bitdefender.onmicrosoft.com/resource/subscriptions/7902f377-3b93-4897-a40d-4d2ea573325f/resourceGroups/ms-openai-hackathon/providers/Microsoft.CognitiveServices/accounts/MS-OpenAI-Hackathon/cskeys)
* [DEPLOYMENT-NAME](https://oai.azure.com/portal/aeb223462b3640b592ca016e87b677bb/deployment?tenantid=487baf29-f1da-469a-9221-243f830c36f3)


Quickstart
----------
1. Clone the repository
2. Install [Python 3.11.3](https://www.python.org/downloads/release/python-3113/)
3. Create a virtual environment (`python -m venv venv`)
4. Activate the virtual environment
   * windows: `venv\Scripts\activate.bat`
   * linux & macos: `source venv/bin/activate` 
5. Install the requirements (`pip install -r requirements.txt`)
6. Configure the environment variables (endpoint & api key) and set the deployment-name in `quickstart.py`
7. Run the quickstart.py script: `python quickstart.py`
