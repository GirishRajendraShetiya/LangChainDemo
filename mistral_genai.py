from langchain_ollama import ChatOllama

llm = ChatOllama(model = "mistral:latest")

question = input("What's your ask: ")
answer = llm.invoke(question).content
print(answer)
