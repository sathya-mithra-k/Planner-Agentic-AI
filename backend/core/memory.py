import json
import os

path = r"C:\Users\sathy\AgenticAI\Planner-Agentic-AI\backend\data\memory.json"

class Memory:
    def __init__(self,path):
        self.path = path

    def read(self):
        with open(self.path,"r") as f:
            return json.load(f)

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

