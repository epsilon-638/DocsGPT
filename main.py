import argparse
from langchain.prompts import PromptTemplate
from agent import agent
from doc_tools import fetch_docs
from prompt import prompt_template

class Repl(argparse.Action):
  def __init__(self, nargs=0, **kw):
    super().__init__(nargs=nargs, **kw)
  def __call__(self, parser, namespace, values, option_string=None):
    print("Enter :q to quit repl\n")
    while True:
      url = input("Enter URL: ")
      if url == ':q': break

      question = input("\nWhat question do you have?: ")
      if question == ':q': break

      print(agent.run(prompt_template.format(url=url, question=question)))

parser = argparse.ArgumentParser()

parser.add_argument(
  "--start-repl",
  action=Repl
)
parser.add_argument(
  "--dry-test",
  action="store_true"
)
parser.add_argument("url", nargs='?')
parser.add_argument(
  "-q",
  "--question",
  nargs='?'
)


args = parser.parse_args()

if __name__ == "__main__":
  if args.url and args.question:
    if args.dry_test:
      fetch_docs(args.url, args.question)
    else:
      print(agent.run(prompt_template.format(url=args.url, question=args.question)))