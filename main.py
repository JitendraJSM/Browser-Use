from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()

import asyncio

api_key = os.getenv("GEMINI_API_KEY")


# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

async def main():
    # Create agent with the model
    agent = Agent(
        task="Open https://www.youtube.com and search videos for top movies on channel @Mr20s get on the first video give me the first 10 comments in list format",
        llm=llm
    )
    result = await agent.run()
    # Print the result
    print(result)

asyncio.run(main())