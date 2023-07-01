from langchain.chat_models import ChatOpenAI
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
planner = load_chat_planner(llm)
executor = load_agent_executor(llm, [doc_tool], verbose=True)
agent = PlanAndExecute(planner=planner, executor=executor, verbose=True)