import time

from revChatGPT.V1 import Chatbot

from config import Config


def ask_chatbot(chat_bot: Chatbot, prompt: str, conversation_id, parent_id):
    prev_text = ""
    for data in chat_bot.ask(prompt, conversation_id, parent_id):
        message = data["message"][len(prev_text) :]
        # print(message, end="", flush=True)
        prev_text = data["message"]
        conversation_id = data["conversation_id"]
        parent_id = data["parent_id"]
    return prev_text, conversation_id, parent_id


def main():
    print(Config.CHATBOT_CONFIG)

    print("start chat")
    start = time.time()
    chatbot = Chatbot(Config.CHATBOT_CONFIG)
    print(f"robot connected: {round(time.time() - start, 3)} seconds")

    print()
    print("---" * 6)
    print("// Hello, there! I'm Chat GPT. How can I help?")
    print("---" * 6)

    conversation_id, parent_id = None, None
    while True:
        print()
        prompt = input("Ask GPT: ")
        if prompt == "exit":
            break
        print()
        print("GPT Reply: ", end="")

        start = time.time()
        try:
            message, conversation_id, parent_id = ask_chatbot(chatbot, prompt, conversation_id, parent_id)
        except Exception as e:
            print(e)
        print(f"robot responsed: {round(time.time() - start, 3)} seconds")

        print()
        print("---" * 6)


if __name__ == "__main__":
    main()
