#!/usr/bin/env python
from crew import InstagramCrew
import datetime
from dotenv import load_dotenv
import os

load_dotenv(override=True)  # take environment variables from .env.

def run():

    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
        'instagram_description': input('Enter the page description here: '),
        'topic_of_the_week': input('Enter the topic of the week here: '),
    }
    InstagramCrew().crew().kickoff(inputs=inputs)

if __name__ == '__main__':
    run()
