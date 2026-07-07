import requests
 
def ask_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
 
# Simple Agent Loop
goal = "Tell me 3 uses of AI"
 
for step in range(2):
    print(f"\nStep {step+1}")
 
    prompt = f"""
You are an AI agent.
 
Goal: {goal}
 
Decide:
- think
- final answer
 
Reply format:
ACTION: <think/final>
INPUT: <text>
"""
 
    output = ask_llm(prompt)
    print(output)
 
    if "final" in output.lower():
        break
 