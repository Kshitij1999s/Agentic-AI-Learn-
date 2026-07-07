from langchain_community.llms import Ollama
 
llm = Ollama(model="llama3")
 
while True:
    user_input = input("You: ")
 
    if user_input.lower() in ["exit", "quit"]:
        print("AI: Goodbye!")
        break
 
    response = llm.invoke(user_input)
    print("AI:", response)