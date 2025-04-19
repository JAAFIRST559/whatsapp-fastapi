from fastapi import FastAPI, Query, HTTPException
import re
import httpx
import os

app = FastAPI()

ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN", "your-access-token")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "your-phone-number-id")
API_URL = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

def validate_phone_number(number: str) -> bool:
    return bool(re.fullmatch(r"^\+\d{10,15}$", number))

@app.get("/send_message")
async def send_message(phone_number: str = Query(..., description="Phone number in E.164 format (e.g., +1234567890)")):
    if not validate_phone_number(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format. Use E.164 format.")

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": "Hello, this is a test message from our TMBC bot!"
        }
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"WhatsApp API error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return {"status": "success", "message": "Message sent successfully."}