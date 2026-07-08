Make it work in VS-Code
------------------------------------------------------------------------------------------------------
Choose the Right Python Interpreter

If VS Code shows a yellow warning line under your import statement, it usually means the editor is looking at a different Python installation than the one you used to install the library.
1.Open the Command Palette by pressing Ctrl + Shift + P (Cmd + Shift + P on macOS).
2.Type Python: Select Interpreter and select it from the list.
3.Choose the Python environment where you just installed your package (look for your active virtual environment or global system path).
4.Right click on file Open in integrated terminal and click on plus and choose command prompt

Python Version 3.12 needed
---------------------------------------------------------------------------------------------------------------------
Create Environment:-------------------

python -m venv langch1
langch1\Scripts\activate.bat

Libraries needed:-------------------------

pip install langchain==0.2.14
pip install langchain-core==0.2.43
pip install langchain-community==0.2.12
pip install langchain-text-splitters==0.2.4
pip install langsmith==0.1.147
pip install langchain-ollama==0.1.3

pip install faiss-cpu
pip install wikipedia
pip install torch --index-url https://download.pytorch.org/whl/cpu
 
ollama pull nomic-embed-text 
