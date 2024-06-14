#!/usr/bin/env python
from crew import ContentPlanningCrew
import datetime
from dotenv import load_dotenv

import logging
import agentops

load_dotenv(override=True)  # take environment variables from .env.
logging.basicConfig(level=logging.DEBUG) # this will let us see that calls are assigned to an agent
agentops.init()

def run():

    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {}
    ContentPlanningCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
