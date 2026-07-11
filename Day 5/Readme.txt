Crew AI ------------------------------------- (write python -m before pip in case of error) (execute code like in cmd {python ""ex.py""})
-------------------------------------------
Environment :-
python -m venv crewAI
 
crewAI\Scripts\activate.bat
--------------------------------------------------
Libraries :-

pip install crewai litellm langchain langchain-community faiss-cpu sentence-transformers

pip install "crewai[litellm]"
 pip install crewai crewai-tools langchain-ollama 

==============================================================================================

PhiDATA------------------

Environment:- 

python -m venv phidata
phidata\Scripts\activate.bat

Libraries :------------------------------------------------------------------------------------------------

pip install phidata ollama
ollama pull llama3.1
ollama pull mistral
pip install -U ddgs
pip install sqlalchemy
