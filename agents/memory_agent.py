import os 
import json
from langchain_ollama import ChatOllama
llm=ChatOllama(model="llama3.1:8b",temperature=0)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(BASE_DIR, "memory.json")
def load_memory():
    if not os.path.exists(data_file):
        return {}
    with open(data_file,"r") as f:
        return json.load(f)
def save_memory(data):
    with open(data_file,"w") as f:
        json.dump(data,f,indent=4)
def ask_mem(message):
    prompt=f"""
You are a memory extraction agent.

Extract personal facts from the user message and return ONLY a raw JSON object.
No explanation. No markdown. No code blocks. Just the JSON.

Look for:
- name: "im X", "i am X", "my name is X", "call me X"
- location: "i live in X", "im from X"
- goal: "i want to be X", "my goal is X"
- skills: "i know X", "i code in X"
- project: "im working on X"

Examples:
message: "hi im aathi" → {{"save": true, "facts": {{"name": "aathi"}}}}
message: "my name is john" → {{"save": true, "facts": {{"name": "john"}}}}
message: "what time is it" → {{"save": false}}
message: "i love python" → {{"save": true, "facts": {{"preference": "loves python"}}}}

User Message: "{message}"

JSON:
"""
    ans=llm.invoke(prompt).content.strip()
    #print("DEBUG ask_mem raw:", ans)
    try:
        return json.loads(ans)
    except:
        return{"save":False}
def memory_agent(message):
    result=ask_mem(message)
    if not result.get("save"):
        return "no memory saved"
    facts=result.get("facts",{})
    data=load_memory()
    for key,value in facts.items():
        if key not in data or not data[key]:
            data[key] = value
    save_memory(data)
    return f"memory saved:{facts}" 

def get_memory():
    return load_memory()