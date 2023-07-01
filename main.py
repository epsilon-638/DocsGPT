import argparse
from langchain.prompts import PromptTemplate
from agent import agent

parser = argparse.ArgumentParser()

parser.add_argument("url")
parser.add_argument(
  "-q",
  "--question",
)

args = parser.parse_args()

prompt = """Fetch the response of the documentation url '{url}' and answer a user question about the contents of the page. Question about the response text: {question}"""
prompt_template = PromptTemplate(
  input_variables=["url", "question"],
  template=prompt,
)

if __name__ == "__main__":
  print(agent.run(prompt_template.format(url=args.url, question=args.question)))