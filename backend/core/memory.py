import json
import os

path = r"C:\Users\sathy\AgenticAI\Planner-Agentic-AI\backend\data\memory.json"

class Memory:
    def __init__(self,path):
        self.path = path
        # Ensure parent directory exists and file is initialized
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path) or os.path.getsize(self.path) == 0:
            with open(self.path, "w") as f:
                json.dump({}, f)

    def read(self):
        try:
            with open(self.path,"r") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def write(self,data):
        with open(self.path,"w") as f:
            json.dump(data,f,indent=4)

    def get(self,key):
        data = self.read()
        return data.get(key)

    def add(self,key,value):
        data = self.read()
        data[key] = value
        self.write(data)

