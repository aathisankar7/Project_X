from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0
)

def route_request(command):

    prompt = f"""
You are Jarvis Router Agent.

Choose ONLY ONE agent:

system → opening apps, closing apps, time, computer control  
search → latest info, news, internet facts, public knowledge  
chat → conversation, greetings, personal questions, memory-based questions  

IMPORTANT:
- Questions about the user (like name, goals, identity) → chat
- Greetings → chat
- Learning/help → chat

Examples:
"hi" → chat
"hello" → chat
"what is my name" → chat
"who am i" → chat
"what should i study" → chat
"open chrome" → system
"what time is it" → system
"latest AI news" → search

User:
{command}

Reply ONLY one word:
system
search
chat
"""

    return llm.invoke(prompt).content.strip().lower()


def router(command):

    agent = route_request(command)

    if "system" in agent:
        from agents.system_agent import run_sys_task
        return run_sys_task(command)

    elif "search" in agent:
        from agents.search_agent import search_agent
        return search_agent(command)

    else:
        from agents.chat_agent import run_chat_task
        return run_chat_task(command)