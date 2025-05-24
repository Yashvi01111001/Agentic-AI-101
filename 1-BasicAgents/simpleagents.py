from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools #for external internet search


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#creating the agent now:
agent = Agent(
    model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    description = "You are an assistant please reply formally and detailed based on the questions",
    tools = [DuckDuckGoTools()],
    markdown = True #to display the output in the form of markdown set it to 'True'
)

agent.print_response("What is Agentic AI and how can it be used for Kenyan Tourism industry?")