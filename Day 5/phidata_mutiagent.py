from phi.agent import Agent
from phi.model.ollama import Ollama
# from phi.tools.duckduckgo import DuckDuckGo   # ⚠️ keep disabled for stability
 
# 🔍 Research Agent
research_agent = Agent(
    name="Researcher",
    role="Find accurate information",
    model=Ollama(id="mistral"),
    instructions=[
        "Give a factual overview of the topic",
        "Keep it concise and informative"
    ],
    # tools=[DuckDuckGo()],  # ⚠️ enable later if needed
    markdown=True,
    debug=True
)
 
# ✍️ Writer Agent
writer_agent = Agent(
    name="Writer",
    role="Write clean and engaging content",
    model=Ollama(id="mistral"),
    instructions=[
        "Write in simple and clear English",
        "Structure with headings and bullet points"
    ],
    markdown=True,
    debug=True
)
 
# 🧪 Reviewer Agent
reviewer_agent = Agent(
    name="Reviewer",
    role="Improve and correct content",
    model=Ollama(id="mistral"),
    instructions=[
        "Fix grammar and clarity",
        "Make output professional and polished"
    ],
    markdown=True,
    debug=True
)
 
# 👇 TASK
topic = "AI agents in 2026"
 
# =========================
# STEP 1: RESEARCH
# =========================
print("\n🔍 STEP 1: RESEARCHING...\n")
 
research = research_agent.run(topic).content
 
print("\n--- RESEARCH OUTPUT ---\n")
print(research)
 
 
# =========================
# STEP 2: WRITING
# =========================
print("\n✍️ STEP 2: WRITING...\n")
 
draft = writer_agent.run(
    f"Write a detailed article using this research:\n{research}"
).content
 
print("\n--- DRAFT OUTPUT ---\n")
print(draft)
 
 
# =========================
# STEP 3: REVIEWING
# =========================
print("\n🧪 STEP 3: REVIEWING...\n")
 
final = reviewer_agent.run(
    f"Improve this article:\n{draft}"
).content
 
print("\n--- FINAL OUTPUT ---\n")
print(final)