from langchain_tavily import TavilySearch
from src.config.settings import settings
from src.services.llm.tool_utils import WatherToolUtils
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
import arxiv


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

    def send_email(self, to:str, subject:str, body:str):
        """
        Send an email to a specified recipient
        """
        print("send email tool executed...............")

        return {
            "to": to,
            "subject": subject,
            "body": body,
            "status": "Email sent successfully"
        }

    def arxiv_search(self):
        """
        Create ArXiv search tool.
        """
        print("arxiv tool executed...............")
        wrapper = ArxivAPIWrapper(
            arxiv_search=arxiv.Search,
            top_k_results=3,
            load_max_docs=1,
            doc_content_chars_max=2000,
            arxiv_exceptions=arxiv.ArxivError
        )

        return ArxivQueryRun(
            api_wrapper=wrapper
        )
        
        

    


tools = Tools()
tool_list = [
    tools.tavily_search(),
    tools.arxiv_search(),
    tools.weather_formatted,
    tools.send_email
    ]