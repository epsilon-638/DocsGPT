from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
import requests

MAX_TOKENS = 4097
chat = ChatOpenAI(temperature=0)

class URLInput(BaseModel):
  url: str = Field()

def fetch_docs(url: str) -> str:
  """Fetch and return response of documentation using a user supplied url"""
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  text = soup.get_text()
  if len(text) > MAX_TOKENS:
    return text[:MAX_TOKENS]

  return text 

doc_tool = StructuredTool.from_function(
  fetch_docs,
  args_schema=URLInput,
)