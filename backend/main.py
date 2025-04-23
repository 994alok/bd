from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins for development; restrict in production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate")
async def calculate(request: Request):
    data = await request.json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    if num1 is None or num2 is None:
        return {"result": "Invalid input"}
    try:
        result = float(num1) + float(num2)
        return {"result": result}
    except Exception:
        return {"result": "Error occurred"}

@app.get("/")
async def root():
    return {"message": "Hello World"}
