import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from learning-langchain!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()

# I am not sure if this is correct, but I am trying to create a simple langchain environment.

# I am just checking if the git is working properly and if I can push to the repository.

import pandas as pd
import numpy as np
 

import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the Chat Model
# The model uses the OPENAI_API_KEY environment variable automatically.
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 2. Define a Prompt Template
# This structures the input to the model.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that tells jokes."),
    ("human", "{question}")
])

# 3. Define an Output Parser
# This ensures the model's response is returned as a clean string.
output_parser = StrOutputParser()

# 4. Create a Chain using LangChain Expression Language (LCEL)
# The pipe symbol (|) connects components sequentially.
chain = prompt | llm | output_parser

# 5. Invoke the chain with an input
response = chain.invoke({"question": "Tell me a joke about a golden retriever!"})

# 6. Print the response
print(response)


