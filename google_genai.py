import os
from langchain_google_genai import ChatGoogleGenerativeAI

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite", api_key = GOOGLE_API_KEY)

question = input("What's your ask: ")
answer = llm.invoke(question).content[0]['text']
print(answer)
