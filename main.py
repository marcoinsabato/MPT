from config.config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI


def main():
    print("Welcome to the interactive shell, now you can chat with your favorite LLM \n Type 'exit' to quit. \n\n\n")
    messages = [];

    while True:    
        user_input = input()

        if user_input.lower() == 'exit':
            print("Exiting the interactive shell.")
            break
        else:
            model = ChatOpenAI(model="gpt-4o")
            messages.append({"role": "user", "content": user_input})

            for r in model.stream(user_input):
                print("\033[94m" + r.content + "\033[0m", end="", flush=True)
                # print("\033[94m" + r.content + "\033[0m")

            print("\n")    
            # Process the command or input
            messages.append({"role": "assistant", "content": r.content})

if __name__ == "__main__":
    main()