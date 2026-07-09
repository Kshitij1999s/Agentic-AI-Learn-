# export LANGSMITH_TRACING=true
# export LANGSMITH_ENDPOINT=https://api.smith.laain.com
# export LANGSMITH_API_KEY=ls4c6983c9f99825f9b33196b7
# export LANGSMITH_PROJECT="agenticailang"

# export OPENAI_API_KEY=<your-openai-api-key>

# site https://smith.langchain.com/

from langsmith import Client
from langchain_community.llms import Ollama
 
# LangSmith client
#client = Client(
#    api_key="ls145aa7557925310e",
#    api_url="https://eu.apiom"
#)
client = Client(
    api_key="lsv2_pt_8_99b331",
    api_url="https://ahain.om"
)
 
# Local Ollama model
ollama = Ollama(model="llama3", temperature=0.7)
 
# Prompt
prompt = "List 3 interesting facts about Neptune."
 
# Call model
result = ollama.invoke(prompt)
 
# Print LLM output
print("LLM Response:\n", result)
 
# Log run manually to LangSmith
client.create_run(
    name="Ollama Llama3 Run",
    run_type="llm",
    inputs={"prompt": prompt},
    outputs={"output": result},
    project_name="agenticaing"
)
 
print("Logged to LangSmith successfully!")
