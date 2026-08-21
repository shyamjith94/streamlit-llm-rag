from langchain_tavily import TavilySearch
from src.config.settings import settings
from src.services.llm.tool_utils import WatherToolUtils
import requests



class Tools(WatherToolUtils):
    def __init__(self):
        self.tool_list = []

    def tavily_search(self):
        """
        Web search content
        """
        print("tavily tool executed...............")
        # print("5"*5, settings.tavily_api_key)
        return TavilySearch(
            tavily_api_key=settings.tavily_api_key,
            max_results=5,
            search_depth="basic",
            topic="news",
        )
    def get_weather(self, city:str):
        """ 
        Get the current city weather informaion
        """
        print("weather tool executed...............")
        return self.weather_formatted(city)


tools = Tools()
tool_list = [
    tools.tavily_search(),
    tools.weather_formatted
    ]