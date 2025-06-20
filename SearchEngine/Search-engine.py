import os

from dotenv import load_dotenv
load_dotenv()

import streamlit as st

# Set environment variables from Streamlit secrets
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = st.secrets["LANGCHAIN_PROJECT"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
groq_api_key = st.secrets["GROQ_API_KEY"]
from langchain_groq import ChatGroq

llm =ChatGroq(groq_api_key=groq_api_key,model="gemma2-9b-it")


# Create Tool
from langchain_community.tools import DuckDuckGoSearchResults
duck_tool=DuckDuckGoSearchResults()

print(duck_tool.name)
print(duck_tool.description)  # -->Each tool in LangChain (like DuckDuckGoSearchRun) has an internal description string that tells the agent:
                              #    What this tool does , When and how it should be used


# List Tools
tools=[duck_tool]

# Create Prompt For Job search
from langchain_core.prompts import ChatPromptTemplate

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Find and show relevent Jobs based on job seeker skills, experience, designation"),
        ("human","skills:{skills}\n,"
                  "experience:{experience}\n,"
                  "preferred role:{role}\n,"
                  "work preference:{preference}(eg.- remote, work from office)\n"
                  "Show only relevant and recent job results.")
    ]
)

# Create Agent
from langchain.agents import initialize_agent, AgentType


#initialize_agent(...) gives you everything — both agent + executor — ready to go. You don't need to manually create or import them separately.
agent=initialize_agent(
    llm=llm,
    tools=tools,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  #-->LLM reads the tool descriptions, understands your query, and reasons about how to use the tool — without any few-shot examples.(ReAct)
    verbose=True
)

st.title("AI Agent for Job Search")
st.text("Enter Your following details for relevent Job Search:")

skills=st.text_input("Enter your top 3 skills")
experience=st.text_input("Enter your years in experience")
role=st.text_input("Enter your preferred role")
preference=st.text_input("Enter your work preference(eg.-remote or work from office)")


# ✅ Trigger search only if all fields are filled
if all([skills, experience, role, preference]):
    # Format the prompt using .format() — you were passing the prompt string directly before!
    user_query = prompt.format(
        skills=skills,
        experience=experience,
        role=role,
        preference=preference
    )



if st.button("Search Jobs"):
    st.info("Finding...")
    
    try:
        response = agent.invoke(user_query)
        st.success(" Search complete!")
        st.write(response["output"])
    except Exception as e:
        st.error("❌ DuckDuckGo rate limit hit. Try again in 1–2 mins.")
        st.code(str(e))