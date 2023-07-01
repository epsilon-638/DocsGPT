from langchain.prompts import PromptTemplate

prompt = """First step, fetch the response of the documentation using both the url: '{url}' as well as a user defined question: '{question}'. Second step, answer a user question about the contents of the page. Question about the response text: {question}"""
prompt_template = PromptTemplate(
  input_variables=["url", "question"],
  template=prompt,
)