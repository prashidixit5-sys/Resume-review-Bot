import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage

model = ChatGroq(model="llama-3.1-8b-instant")

st.set_page_config(page_title="Resume Reviewer", page_icon="📄")
st.title("📄 Resume Review Bot")
 

if "review" not in st.session_state:
    st.session_state.review = None
if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False
 
resume = st.text_area("Paste your resume here:", height=300)
 
if st.button("Review My Resume"):
    if resume.strip() == "":
        st.warning("Please paste your resume first.")
    else:
        with st.spinner("Reviewing your resume..."):
            messages = [
                SystemMessage(content="""You are an expert resume reviewer for engineering students.
When given a resume, review it and give feedback on:
1. Overall impression
2. Skills section
3. Projects section
4. Education section
5. What's missing
6. What to improve
7. Rate it out of 10
Be honest, helpful and specific"""),
                HumanMessage(content=resume)
            ]
            response = model.invoke(messages)
 
        st.session_state.review = response.content
        st.session_state.feedback_submitted = False  # reset feedback for a new review
 

if st.session_state.review:
    st.subheader("Feedback:")
    st.write(st.session_state.review)
 
    st.divider()
    st.subheader("Was this review helpful?")
 
    if not st.session_state.feedback_submitted:
        col1, col2 = st.columns(2)
        with col1:
            thumbs_up = st.button("👍 Helpful")
        with col2:
            thumbs_down = st.button("👎 Not Helpful")
 
        comment = st.text_area("Any additional comments? (optional)", key="feedback_comment_input")
 
        if thumbs_up or thumbs_down:
            st.session_state.feedback_submitted = True
            st.session_state.feedback_rating = "Helpful" if thumbs_up else "Not Helpful"
            st.session_state.saved_comment = comment
            st.rerun()
    else:
        st.success(f"Thanks for your feedback: **{st.session_state.feedback_rating}**")
        if st.session_state.get("saved_comment"):
            st.caption(f"Your comment: {st.session_state.saved_comment}")
 
        if st.button("Submit another review"):
            st.session_state.review = None
            st.session_state.feedback_submitted = False
            st.rerun()