import time
from pathlib import Path
from typing import Union

from revChatGPT.V1 import Chatbot

from config import Config


def ask_chatbot(chatbot: Chatbot, prompt: str, conversation_id, parent_id):
    prev_text = ""
    for data in chatbot.ask(prompt, conversation_id, parent_id):
        message = data["message"][len(prev_text) :]
        # print(message, end="", flush=True)
        prev_text = data["message"]
        conversation_id = data["conversation_id"]
        parent_id = data["parent_id"]
    return prev_text, conversation_id, parent_id


def init_chatbot(email: str, password: str, proxy: Union[str, None], token_path: Path) -> Union[Chatbot, None]:
    def update_token(headers, token_path: Path):
        bearer = headers.get("Authorization")
        if bearer and isinstance(bearer, str) and "Bearer " in bearer:
            token = bearer[len("Bearer ") :].strip()
            token_path.write_text(token)

    token = token_path.read_text()
    if token:
        max_retry = 3
        while max_retry > 0:
            try:
                chatbot = Chatbot({"access_token": token})
                return chatbot
            except Exception:
                max_retry -= 1

    else:
        max_retry = 3
        while max_retry > 0:
            try:
                chatbot = Chatbot({"email": email, "password": password, "proxy": proxy})
                update_token(chatbot.session.headers, token_path)
                return chatbot
            except Exception:
                max_retry -= 1
    return None


def main():

    print("start chat")
    start = time.time()
    chatbot = init_chatbot(Config.EMAILE, Config.PASSWORD, Config.PROXY, Config.ACCESS_TOKEN_PATH)
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
