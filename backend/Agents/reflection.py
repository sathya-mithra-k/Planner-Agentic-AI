from backend.core.memory import Memory
from backend.core.llm_engine import ask_llm

m = Memory(r"C:\Users\sathy\AgenticAI\Planner-Agentic-AI\backend\data\memory.json")

def analyse(summary):
    prompt = f"You are my personal assistant and reflection agent.Analyse the summary of the day and provide a reflection on the day: {summary}, also provide 2 key learnings and 1 improvement."
    reflection = ask_llm(prompt)
    m.add("reflection", reflection)
    return reflection

print(analyse("I worked hard, exercised, but didn’t sleep much."))
