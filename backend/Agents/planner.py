from backend.core.memory import Memory
from backend.core.llm_engine import ask_llm

m = Memory(r"C:\Users\sathy\AgenticAI\Planner-Agentic-AI\backend\data\memory.json")

def create_plan(goal):
    prompt = f"You are my personal assistant and planner.Create a plan to achieve the goal: {goal}"  
    plan = ask_llm(prompt)
    m.add(goal, plan)
    return plan