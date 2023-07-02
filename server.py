from fastapi import FastAPI
from pydantic import BaseModel
from agent import agent
from prompt import prompt_template

app = FastAPI()

class QuestionRequest(BaseModel):
  url: str
  question: str

@app.post("/api/answer-question")
def answer_question(req: QuestionRequest):
  question_prompt = prompt_template.format(
    url=req.url,
    question=req.question,
  )

  response = agent.run(question_prompt)
  return { "response": response }