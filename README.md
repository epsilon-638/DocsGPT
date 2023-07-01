# DocsGPT

Quick insights from docs & references. Given any URL and a question DocsGPT will respond using the document as context.

## Example
```
export OPENAI_API_KEY="sk-..."
pip install -r requirements.txt
python main.py
```

In this example the GPT Agent fetches the results of the url https://sre.google/sre-book/production-environment/' and is asked the question: What is Borg?

## Response
```
Response: Borg is a cluster management system developed by Google for running large-scale distributed workloads.
```

## TODO
- [ ] Add FastAPI server
- [ ] Create a UI to interact with the agent
- [ ] Store document embeddings and create 'sessions'