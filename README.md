# DocsGPT

Quick insights from docs & references. Given any URL and a question DocsGPT will respond using the document as context.

## Setup
```
cd DocsGPT
export OPENAI_API_KEY="sk-..."
pip install -r requirements.txt
```

## Examples

Google SRE Chapter
```
python3 main.py https://sre.google/sre-book/production-environment/ --question "What is Borg?"
```

Output
```
Response: Borg is a cluster management system developed by Google for running large-scale distributed workloads.
```

In this example the GPT Agent fetches the results of the url https://sre.google/sre-book/production-environment/' and is asked the question: What is Borg?

---

Attention Is All You Need (PDF)
```
python3 main.py https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf --question "What is multi-head attention?"
```

Output
```
Response: Multi-head attention is a type of attention mechanism used in neural networks that allows the model to attend to different parts of the input sequence simultaneously. It is a form of self-attention that allows the model to focus on different parts of the input sequence at the same time.
```

In this example the GPT Agent is able to fetch and parse the PDF and answer the question pertaining to Multi-Head Attention in the context of this famous Google Research Paper.

## REPL

Start REPL
```
python3 main.py --start-repl
```

REPL
```
Enter :q to quit repl

Enter URL: example.com/confusing-documentation

What question do you have?: How does this confusing thing work?
```

## TODO
- [x] Add CLI
- [x] Add REPL
- [ ] Add FastAPI server
- [ ] Create a UI to interact with the agent
- [x] Compare portions of text using document comparison and grab the most relevant bodies of text to the given question.
- [ ] Store document embeddings and create 'sessions'