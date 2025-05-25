from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools #for external internet search
from agno.tools.yfinance import YFinanceTools #for financial data retrieval 

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

web_agent = Agent(
    name = "Web Agent",
    role = "Search the web for information",
    model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    tools = [DuckDuckGoTools()],
    instructions = "Always include the sources",
    show_tool_calls=True,
    markdown = True
)

finance_agent = Agent(
    name = "Finance Agent",
    role = "Retrieve financial data and analyze stock market trends",
    model = OpenAIChat(id="gpt-3.5-turbo "),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    instructions = "Use neat tables to display data clearly",
    show_tool_calls=True,
    markdown = True
)

agent_team = Agent(
    team = [web_agent, finance_agent],
    model = Groq(id="meta-llama/llama-4-scout-17b-16e-instruct"),
    instructions = ["Always include sources", "Use tables to display data clearly"],
    show_tool_calls=True,
    markdown = True
)

agent_team.print_response("What are the latest trends in the Kenyan tourism industry and how can they be leveraged for investment opportunities? Also, provide insights on the current stock performance of major tourism companies in Kenya.")
# This code creates a multi-agent system where one agent searches the web for tourism trends and another retrieves financial data on tourism companies.
# The agents collaborate to provide a comprehensive response, including sources and data in a clear format.