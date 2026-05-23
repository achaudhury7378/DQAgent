from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="gemma4:26b")

response = llm.invoke("Explain transformers in one sentence")
print(response)