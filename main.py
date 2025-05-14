from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "MELANIE is online and listening."}

@app.post("/add_note")
async def add_note(request: Request):
    body = await request.json()
    deal_id = body.get("deal_id")
    content = body.get("note")

    # ✅ Securely load your API key from the Render environment variable
    api_key = os.getenv("PIPEDRIVE_API_KEY")
    url = f"https://api.pipedrive.com/v1/notes?api_token={api_key}"

    payload = {
        "content": content,
        "deal_id": deal_id
    }

    response = requests.post(url, json=payload)
    return {"status": "sent", "response": response.json()}
