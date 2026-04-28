from langchain_ollama import ChatOllama
from agents.memory_agent import get_memory
llm=ChatOllama(model="llama3.1:8b",temperature=0.5)
def run_chat_task(command):
    memory=get_memory()
    memory_text="\n".join([f"{k}:{v}" for k,v in memory.items()])
    prompt=f"""
You are Jarvis, a smart personal assistant.

User Profile:
{memory_text}

Instructions:
- Use memory if needed 
- Be short, clear, and helpful
STRICT RULES:
- If user asks about their anything use ONLY the memory above
- NEVER guess or invent personal details
- If info exists in memory → MUST use it 
dont bring names thats not in memory_text (user profile)

User:
{command}
"""
    answer=llm.invoke(prompt).content
    return answer
if __name__ == "__main__":
    print("jarvis chat agent online")
    while True:
        user=input("you:")
        if user.lower()=="exit":
            print("jarvis:good bye boss")
            break
        reply=run_chat_task(user)
        print("Jarvis", reply)





