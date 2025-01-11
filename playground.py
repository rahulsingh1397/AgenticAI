from phi.agent import Agent
import phi.api
from phi.model.groq import Groq #Model
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
import phi
from phi.playground import Playground, serve_playground_app

#load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## Web Search Agent
web_search_agent = Agent(
    name = "Web search agent",
    role = "Search the web for information",
    model= Groq(id="llama-3.1-70b-versatile"),
    tool= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls = True,
    markdown=True,
)

## Financial agent
finance_agent =Agent(
name = "Finance AI Agent",
model = Groq(id="llama-3.1-70b-versatile"),
tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
instructions = ["Use tables to display the data"],
show_tool_calls = True,
markdown=True,
)

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app",reload=True)
