# main.py
import os
from router import router
from agents.memory_agent import memory_agent

print("🔥 Jarvis Online (type exit)")

while True:

    user = input("You: ").strip()

    if not user:
        continue

    if user.lower() == "exit":
        print("Jarvis: Goodbye boss 😎")
        break

    try:
        result = memory_agent(user)
        #print("DEBUG memory_agent result:", result)
        #print("DEBUG memory file exists:", os.path.exists("agents/memory.json"))
        reply = router(user)

        print("Jarvis:", reply)

    except Exception as e:
        print("Jarvis Error:", e)