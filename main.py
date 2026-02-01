from fastapi import FastAPI

app = FastAPI(title="FastAPI GitHub → Replit Demo")

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}
