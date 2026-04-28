import requests
from langchain_ollama import ChatOllama
llm=ChatOllama(model="llama3.1:8b",temperature=0.2)
serper_api_key="9a4ff1c3b485eba4acecb29eeffa277f58e2b3fe"
def google_query(query):
    url="https://google.serper.dev/search"
    payload={"q":query}

    headers = {
        "X-API-KEY":serper_api_key,
        "Content-Type": "application/json"}

    response=requests.post(url,json=payload,headers=headers)
    return response.json()
    

def search_agent(command):
    data=google_query(command)
    organic=data.get("organic",[])[:5]
    text=""
    for i in organic:
        title=i.get("title","")
        snippet=i.get("snippet","")
        link=i.get("link","")
        text+=f"title:{title}\n"
        text+=f"snippet:{snippet}\n"
        text+=f"link:{link}\n"
    prompt = f"""
You are Jarvis Search Agent.

Summarize these search results clearly.

Search Query:
{command}

Results:
{text}
Your job:
- Summarize clearly
- Give top useful answers
- Use bullet points
- Be short and smart
- If asking for best places/products, rank top 3

"""
    answer=llm.invoke(prompt).content.strip()
    return answer
if __name__ =="__main__":
    print("jarvis search agent online")
    while True:
        user=input("you:")
        if user.lower()=="exit":
            print("goodbye boss")
            break
        reply=search_agent(user)
        print("jarvis:",reply)


