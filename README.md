# Project X: Jarvis AI Assistant

A localized, autonomous AI assistant powered by LangChain and Ollama. 

## Features

- **Multi-Agent Architecture**: Uses a smart router to delegate tasks to specialized agents.
- **System Control (`system_agent`)**: Controls local computer applications and retrieves system information (e.g., opening apps, getting the time).
- **Web Search (`search_agent`)**: Performs online queries to fetch real-time data, news, and facts.
- **Conversational AI (`chat_agent`)**: Handles general chatting, answering personal questions, and processing context-dependent queries.
- **Memory Management (`memory_agent`)**: Persists conversational state and memory variables across sessions.

## Tech Stack

- **Python**
- **LangChain**
- **Ollama** (Running the `llama3.1:8b` model locally)

## How to Run

1. Make sure you have Ollama installed and the `llama3.1:8b` model pulled:
   ```bash
   ollama pull llama3.1:8b
   ```

2. Install the required Python dependencies:
   ```bash
   pip install langchain-ollama
   ```

3. Run the main assistant loop:
   ```bash
   python main.py
   ```

4. Type your command when prompted with `You:` and enjoy conversing with Jarvis! (Type `exit` to quit).
