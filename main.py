from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "MELANIE is online and listening."}
