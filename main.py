from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operator: str

@app.post("/calculate")
def calculate(req: CalculationRequest):
    if req.operator == "+":
        result = req.num1 + req.num2
    elif req.operator == "-":
        result = req.num1 - req.num2
    elif req.operator == "*":
        result = req.num1 * req.num2
    elif req.operator == "/" and req.num2 != 0:
        result = req.num1 / req.num2
    elif req.operator == "/" and req.num2 == 0:
        result = "Error: division by zero"
    else:
        result = "Error: invalid operator"
    return {"result": result}

@app.get("/")
def root():
    return {"app": "Build A Full Stack Application For", "status": "running", "generated_by": "VIA"}

@app.get("/health")
def health():
    return {"status": "healthy"}
    

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
