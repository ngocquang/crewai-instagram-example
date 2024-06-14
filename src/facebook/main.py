#!/usr/bin/env python
from crew import FacebookCrew
import datetime
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # take environment variables from .env.

def run():

    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'topic_of_the_week': input('Enter the topic of the week here: '),
    }
    FacebookCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
