from langchain_community.llms import Ollama
import requests

# -----------------------------
# LLM call (Ollama)
# -----------------------------
def call_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
 
# -----------------------------
# AGENT LOOP
# -----------------------------
def agent(goal):
    memory = []
 
    for step in range(3):
        print(f"\n--- Step {step+1} ---")
 
        context = "\n".join(memory)
 
        prompt = f"""
You are an AI agent.
 
Goal: {goal}
 
Previous steps:
{context}
 
Follow this cycle:
1. PLAN: What to do next
2. EXECUTE: Perform step
3. OBSERVE: What happened
4. REFLECT: Improve
 
Respond strictly in format:
 
PLAN: ...
EXECUTE: ...
OBSERVE: ...
REFLECT: ...
"""
 
        output = call_llm(prompt)
        print(output)
 
        # store in memory
        memory.append(output)
 
        # stopping condition
        if "FINAL" in output.upper():
            print("\n✅ Task Completed")
            break
 
# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    llm = Ollama(model="llama3")
 
while True:
    user_input = input("You: ")
 
    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye!")
        break
 
    response = llm.invoke(user_input)
    print("AI:", response)