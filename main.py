import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from learning-langchain!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()

# I am not sure if this is correct, but I am trying to create a simple langchain environment.
