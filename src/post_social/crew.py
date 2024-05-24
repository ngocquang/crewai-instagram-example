
import openai
from crewai import Agent, Task, Crew, Process

from langchain.agents import load_tools
import os

from langchain_openai import ChatOpenAI

OPENAI_MODEL_NAME= 'gpt-4o'

llm=ChatOpenAI(model_name=OPENAI_MODEL_NAME)

# Defining tools
human_tools = load_tools(["human"])

market_researcher = Agent(
role = 'Market Researcher',
goal='Research new and emerging trends in the mobile game in Philippines',
backstory = 'You are a market researcher in the mobile game industry',
verbose= True,
allow_delegation= False,
    llm=llm
)

campaign_creator =  Agent(
role = 'Marketing Campaign Creator',
goal='Come up with 3 interesting marketing campaign ideas in the mobile game industry based on market research insights',
backstory = 'You are a marketing campaign planner in the mobile game industry',
verbose= True,
allow_delegation= False,
llm=llm,
# tools=human_tools
)

digital_marketer =  Agent(
role = 'Digital Marketing Content Creator',
goal='Come up with 2 or 3 interesting advertisement ideas for marketing on digital platforms such as Facebook, Instagram along with script for each marketing campaign',
backstory = 'You are a marketing marketer specialising in performance marketing in the mobile game industry',
verbose= True,
allow_delegation= False,
    llm=llm
)



def run(inputs):

    task1 = Task(description=inputs["prompt1"],
        expected_output = 'New and Emerging Market Trends in the Card Game Pusoy ZingPlay in Philippines in 2024',
        agent=market_researcher)

    task2 = Task(description=inputs["prompt2"],
        expected_output = 'Digital Marketing Campaign ideas based on the market trends which have the potential to go viral on Facebook, Instagram',
        agent=campaign_creator)

    task3 = Task(description=inputs["prompt3"],
        expected_output = """Weekly posts with SEO friendly hashtags for social media platforms like Facebook, Instagram.
        Example post:
    👉 COM.MENT THE RANKG
    🤩 Have you memorized all the poker rank by heart? Answer this quiz to double check your knowledge!
    ---------------------------------------------
    👉 Download now:
    🔥 ANDROID: https://rebrand.ly/pusoyzingplay
    🔥 IOS: https://apps.apple.com/ca/app/pusoy-zingplay-outsmart-fate/id1636802011
    #ZingPlay #PusoyZingPlay #ZingPlayFamily #AmaZingPlay
        """,
        agent=digital_marketer)

    # Create crew
    crew = Crew(
        agents=[market_researcher,campaign_creator,digital_marketer],
        tasks=[task1,task2,task3],
        verbose = 2,
        process = Process.sequential
    )
    # kick-off the tasks
    return crew.kickoff(),task1,task2,task3
