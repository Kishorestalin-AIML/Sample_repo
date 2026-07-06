from gpt4all import GPT4All

model = GPT4All("Phi-3-mini-4k-instruct.Q4_0.gguf")


system_prompt = """
You are Luna.

You are a caring, affectionate virtual companion.
You speak warmly and naturally.
You encourage the user.
"""

with model.chat_session():
    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        response = model.generate(
            user,
            max_tokens=80,
            temp=0.7
        )

        print("Bot:", response)