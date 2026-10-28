from llm import call_model

with open("prompts/system.md", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# the model has no memory: this list IS the conversation
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

while True:
    user_input = input("you: ").strip()
    if user_input in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})
    reply = call_model(messages)
    messages.append(reply)  # append the assistant message so the next turn remembers it

    print("agent:", reply["content"])