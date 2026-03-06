from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# --- CONFIG ---
VAPI_API_KEY = "***REMOVED***"
VAPI_ASSISTANT_ID = "***REMOVED***"
VAPI_PHONE_NUMBER_ID = "***REMOVED***"
USER_PHONE_NUMBER = "***REMOVED***"

def trigger_voice_call(symbol, price, score, reason, risk_level, user_phone_number):
    url = "https://api.vapi.ai/call"
    headers = {"Authorization": f"Bearer {VAPI_API_KEY}", "Content-Type": "application/json"}

    assistant_overrides = {
        "variableValues": {
            "symbol": str(symbol),
            "price": str(price),
            "score": str(int(score)),
            "reasoning": str(reason),
            "risk": str(risk_level)
        }
    }

    payload = {
        "assistantId": VAPI_ASSISTANT_ID,
        "phoneNumberId": VAPI_PHONE_NUMBER_ID,
        "customer": {"number": user_phone_number},
        "assistantOverrides": assistant_overrides
    }

    try:
        print(f"☎️ Dialing {user_phone_number} for {symbol}...")
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 201:
            print(f"✅ Call Initiated!")
            return True
        else:
            print(f"❌ Vapi Error: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return False

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from pydantic import BaseModel

class CallRequest(BaseModel):
    phoneNumber: str

@app.post("/call")
async def make_call(request: CallRequest):
    # Example values for the call, these could come from a form or other input
    symbol = "SOL"
    price = 145.50
    score = 95
    reason = "Solana has huge momentum. This is a real test."
    risk_level = "High"

    if trigger_voice_call(symbol, price, score, reason, risk_level, request.phoneNumber):
        return {"message": "Call initiated successfully!"}
    else:
        return {"message": "Failed to initiate call."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)