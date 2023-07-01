from langchain.tools import StructuredTool
from langchain.chat_models import ChatOpenAI
from pydantic import BaseModel, Field
from bs4 import BeautifulSoup
import spacy
import requests

MAX_TOKENS = 1000
SCORE_THRESHOLD = 0.5
chat = ChatOpenAI(temperature=0)
nlp = spacy.load("en_core_web_lg")

class URLInput(BaseModel):
  url: str = Field()
  question: str = Field()

def fetch_docs(url: str, question: str) -> str:
  """Fetch and return response of documentation using a user supplied url and question, this function requires both a url and a question"""
  question_doc = nlp(question)
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  text = soup.get_text()

  lines = text.splitlines()
  striped_lines = list(filter(lambda l: len(l.strip()), lines))

  scores = [(question_doc.similarity(nlp(l)), l) for l in striped_lines]
  top_scores = list(filter(lambda l: l[0] > SCORE_THRESHOLD, scores))
  top_scores_sorted = sorted(top_scores, key=lambda s: s[0], reverse=True)

  relevant_text = ' '.join([t[1] for t in top_scores_sorted])
  if len(relevant_text) > MAX_TOKENS:
    return relevant_text[:MAX_TOKENS]
  return relevant_text

doc_tool = StructuredTool.from_function(
  fetch_docs,
  args_schema=URLInput,
)