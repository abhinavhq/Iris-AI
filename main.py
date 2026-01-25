import requests
import datetime

MODEL = "llama3"
OLLAMA_URL = "http://localhost:11434/api/generate"

def run_llm(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return response.json()["response"]

def agent_think(user_input):
    system_prompt = f"""
You are Iris, a calm and intelligent AI assistant

Date: {datetime.date.today()}

Your job:
You are Iris, a calm, friendly, and intelligent AI assistant and companion.
Your role is to help the user with a wide range of topics, questions, and tasks,
including learning, problem-solving, creativity, technology, and everyday life.
Adapt your tone and depth based on the situation, and be clear, practical, 
and helpful rather than overly verbose.

User input:
{user_input}

AI response:
"""
    return run_llm(system_prompt)

print("🌸 Iris is online (type 'exit' to quit)\n")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Agent stopped.")
        break

    reply = agent_think(user)
    print("\nIris:", reply, "\n")