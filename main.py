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

