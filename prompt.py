from langchain.prompts import PromptTemplate

prompt = """Fetch the response of the documentation url '{url}' and answer a user question about the contents of the page. Question about the response text: {question}"""
prompt_template = PromptTemplate(
  input_variables=["url", "question"],
  template=prompt,
)