# This script will connect to an existing instance(which is opened with remote debugging port 9222 using "--remote-debugging-port=9222")of Chrome and run the agent

from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from pydantic import SecretStr
import os
import asyncio

from dotenv import load_dotenv
load_dotenv()


browser = Browser(
	config=BrowserConfig(
		headless=False,
		cdp_url='http://localhost:9222',
	)
)
controller = Controller()


# Initialize the model
api_key = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))


async def main():
	task = 'Check URL of all opened tabs is there any tab with url "chrome://privacy-sandbox-dialog/notice" if yes then click on button having text "Got it" else just ignore'
	task += 'Open https://www.youtube.com'
	task += 'search for best movie'
	task += 'click on subscribe'
	task += 'click popup to sign in'
	task += 'do all the thing as to create a personal gmail account'
	task += 'first name is rani, last name is mali, date of birth is 25 june 2005'
	task += 'password must be hhjsm001 and create email as ranimalihhjsm@gmail.com'
	agent = Agent(
		task=task,
		llm=llm,
		controller=controller,
		browser=browser,
	)
	result = await agent.run()
	# Print the result
	print(result)

asyncio.run(main())
