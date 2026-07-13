from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """

    print(f"Searching for: {query}")
    return tavily.search(query=query)

# llm = ChatOllama(model="gemma4:e4b")
llm = ChatOpenAI(model="gpt-5")

tools = [search]
agent = create_agent(
    model=llm,
    tools=tools
)

def main():
    print("Hello from search-agent!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Bay area (or surrounds) on linkedin and list their details")})
    print(result)

if __name__ == "__main__":
    main()