from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner
)
from langchain.agents.tools import Tool
from langchain.llms import OpenAI
from doc_tools import doc_tool

chat = ChatOpenAI(temperature=0)
llm = OpenAI(temperature=0)
tools = [
  Tool(
    name="Fetch Documentation",
    func=doc_tool.run,
    description="Fetch and return response of documentation using a user supplied url",
  ),
]

planner = load_chat_planner(llm)
executor = load_agent_executor(llm, tools, verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)

prompt = """Fetch the response of the documentation url '{url}' and answer a user question about the contents of the page. Question about the response text: {question}"""

prompt_template = PromptTemplate(
  input_variables=["url", "question"],
  template=prompt,
)

url = "https://sre.google/sre-book/production-environment/"
question = "What is Borg?"

print(agent.run(prompt_template.format(url=url, question=question)))