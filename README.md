#  AI Agent Job Search

This project is an intelligent job search assistant powered by **LangChain agents**, **Groq LLM (Gemma-2B-IT)**, and **DuckDuckGo Search tool**. It takes in the user's **skills, experience, preferred role, and work preference**, then intelligently searches and filters job listings in real-time — mimicking how a human agent would think and act.

##  Live Demo

 [Click here to use the AI Job Search Agent](https://ai-agent-job-search-mayank.streamlit.app/)

---

##  Features

-  Searches real-time job data using **DuckDuckGo**
-  Uses **ReAct Agent** from LangChain for reasoning
-  Prints **thoughts, actions, observations**, and final answers
-  Dynamically adapts based on user's input
-  Streamlit interface for easy user interaction

---

##  Tech Stack

- **LLM**: [Gemma 2B IT via Groq](https://groq.com/)
- **LangChain**: Agent + Tooling
- **DuckDuckGo Search Tool**
- **Streamlit**: Frontend UI
- **Python**: Backend logic

---

##  Project Structure

```bash
SearchEngine/
├── .env # Contains your API keys (excluded in .gitignore)
├── requirements.txt # Python dependencies
└── Search-engine.py # Main Streamlit app
```

---

##  Setup Instructions (Locally)

1. **Clone the repo**

```bash
git clone https://github.com/MayankSethi27/AI-Agent-Job-Search.git
cd AI-Agent-Job-Search/SearchEngine
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```
3. **Set up environment variables**
```bash
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
GROQ_API_KEY=your_groq_api_key
```
4. **Run the app**
```bash
streamlit run Search-engine.py
```
---
## How It Works (Internally)
The LangChain ReAct Agent decides which tool to use and what to query.

It uses the DuckDuckGoSearchResults tool to fetch job data.

You’ll see internal reasoning steps like:

- Thought

- Action

- Observation

- The final response is printed based on all intermediate steps.
---
## Dependencies
Check requirements.txt, but mainly includes:

- streamlit

- langchain

- langchain-community

- duckduckgo-search

- python-dotenv

---
## Author
Mayank Sethi

