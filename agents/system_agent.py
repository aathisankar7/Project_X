import subprocess
from datetime import datetime
from langchain_ollama import ChatOllama
import json
llm=ChatOllama(model="llama3.1:8b",temperature=0)
def open_app(app_name):
    subprocess.run(["open","-a",app_name])
    return f"opened{app_name}"

def get_time():
    now=datetime.now().strftime("%I:%M %p")
    return f"current time is {now}"

def speak(text):
    subprocess.run(["say",text])
    return f"spoke{text}"
def ask_ai(command):
    prompt=f"""You are Jarvis System Agent.

Choose one tool.

If user wants to open app:
{{"tool":"open_app","app_name":"Safari"}}

If user wants time:
{{"tool":"get_time"}}

If user wants speaking:
{{"tool":"speak","text":"Hello boss"}}

If not system request:
{{"tool":"none"}}

User request:
{command}

Return only JSON.
"""
    answer=llm.invoke(prompt).content
    return answer
def run_sys_task(command):
    ask_reply=ask_ai(command)
    data=json.loads(ask_reply)
    tool=data["tool"]
    if tool=="open_app":
        result=open_app(data["app_name"])
    elif tool=="get_time":
        result=get_time()
    elif tool=="speak":
        result=speak(data["text"])
    else:
        result="tool not found"
    return result

if __name__ == "__main__":

    while True:
        user = input("You: ")

        if user.lower() == "exit":
            break

        output = run_sys_task(user)
        print(output)

