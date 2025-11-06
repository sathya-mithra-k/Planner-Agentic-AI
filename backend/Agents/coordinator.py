from backend.Agents.planner import create_plan
from backend.Agents.reflection import analyse
from backend.core.llm_engine import ask_llm

class Coordinator:
    def __init__(self):
        self.plan = create_plan
        self.reflect = analyse
        self.ask_llm = ask_llm

    def run(self,msg):
        m = msg.lower()
        if any(k in m for k in ["plan","schedule","task","goals"]):
            return self.plan(msg)
        elif any(k in m for k in ["reflect","analyze","review","summary"]):
            return self.reflect(msg)
        else:
            return self.ask_llm(f"You are a helpful assistant. Please help me with {msg}")
            

