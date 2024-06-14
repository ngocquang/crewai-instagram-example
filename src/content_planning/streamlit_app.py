import streamlit as st
from crew import ContentPlanningCrew  # Import the ResearchCrew class from main.py
import os
import datetime

from dotenv import load_dotenv
load_dotenv(override=True)  # take environment variables from .env.

st.title('Facebook Crew Setup')

with st.sidebar:
    st.header('Enter Your information')
    topic_of_the_week = st.text_area("Enter the topic of the week here:")

if st.button('Run Research'):
    if not topic_of_the_week:
        st.error("Please fill all the fields.")
    else:
        inputs = {
            'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'topic_of_the_week': topic_of_the_week,
        }
        result = ContentPlanningCrew().crew().kickoff(inputs=inputs)
        st.subheader("Results of your research project:")
        st.write(result)
