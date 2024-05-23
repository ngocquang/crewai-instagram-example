import streamlit as st
from crew import InstagramCrew  # Import the ResearchCrew class from main.py
import os
import datetime

from dotenv import load_dotenv
load_dotenv(override=True)  # take environment variables from .env.

st.title('Instagram Crew Setup')

with st.sidebar:
    st.header('Enter Your information')
    instagram_description = st.text_area("Enter the page description here:")
    topic_of_the_week = st.text_area("Enter the topic of the week here:")

if st.button('Run Research'):
    if not instagram_description or not topic_of_the_week:
        st.error("Please fill all the fields.")
    else:
        inputs = {
            'current_date': datetime.datetime.now().strftime("%Y-%m-%d"),
            'instagram_description': instagram_description,
            'topic_of_the_week': topic_of_the_week,
        }
        result = InstagramCrew().crew().kickoff(inputs=inputs)
        st.subheader("Results of your research project:")
        st.write(result)
