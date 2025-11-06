from fastapi import FastAPI, Query
from backend.Agents.coordinator import Coordinator

app = FastAPI()
c = Coordinator()

@app.get("/query")
def query(message: str = Query("")):
    response = c.run(message)
    return {"reply": response}
