from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Browser, BrowserConfig
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()

import asyncio

# Configure the browser to connect to your Chrome instance with Profile 2
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        extra_chromium_args=['--profile-directory=Profile 2']
    )
)

# Initialize the model
api_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

async def main():
    # Create agent with the model
    agent = Agent(
        task="Open https://www.youtube.com and search videos for top movies Mr20s get on the first video give me the first 10 comments in list format",
        llm=llm,
        browser=browser
    )
    result = await agent.run()
    # Print the result
    print(result)

asyncio.run(main())