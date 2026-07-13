from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


# llm = ChatOllama(model="gemma4:e4b")
llm = ChatOpenAI(model="gpt-5")

tools = [TavilySearch()]
agent = create_agent(
    model=llm,
    tools=tools
)

def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Bay area (or surrounds) and list their details")})
    print(result)

if __name__ == "__main__":
    main()