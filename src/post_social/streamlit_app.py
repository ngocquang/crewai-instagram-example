import streamlit as st
from crew import run # Import the ResearchCrew class from main.py
import os
import datetime

from dotenv import load_dotenv
load_dotenv(override=True)  # take environment variables from .env.

st.title('Post Social Crew Setup')

with st.sidebar:
    st.header('Enter Your information')
    # instagram_description = st.text_area("Enter the page description here:")
    # topic_of_the_week = st.text_area("Enter the topic of the week here:")

    prompt1 = st.text_area("What Market Research Task would You like me to do Today?")
    prompt2 = st.text_area("What Marketing Campaigns would You like me to come up with Today?")
    prompt3 = st.text_area("What Digital Marketing Content would You like me to generate Today?")


if st.button('Generate'):
    if not prompt1 or not prompt2 or not prompt3:
        st.error("Please fill all the fields.")
    else:
        with st.spinner("Generating response..."):
            result, task1, task2, task3 = run({"prompt1":prompt1,"prompt2":prompt2,"prompt3":prompt3})
            st.write(result)
            st.write(task1.output)
            st.write(task2.output)
            st.write(task3.output)
