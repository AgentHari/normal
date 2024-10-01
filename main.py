from package1.package1p1 import p1function1
from package2.package2p1 import p1function, needInput
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputModel(BaseModel):
    in1: str

@app.get("/")
def ping():
    return {
        "status": "working"
    }

@app.get("/package1")
def package1p1function1():
    return {
        "status": "working",
        "data": p1function1()
    }

@app.get("/package2")
def package2p1function():
    return {
        "status": "working",
        "imported from another file": True,
        "data": p1function()
    }

@app.post("/input")
def package2p1needInput(data: InputModel):
    return {
        "status": "working",
        "imported from another file": True,
        "data": needInput(in1=data.in1)
    }
