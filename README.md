# WhatsApp Messaging via FastAPI

This FastAPI app sends WhatsApp messages using Meta's WhatsApp Business API.

## 🚀 Features

- Endpoint: `/send_message`
- Message: `"Hello, this is a test message from our TMBC bot!"`
- Accepts phone number as a query parameter in E.164 format (e.g., +1234567890)
- Includes phone number validation and error handling

## 🧰 Tech Stack

- Python
- FastAPI
- Meta WhatsApp Cloud API
- httpx

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/JAAFIRST559/whatsapp-fastapi.git
cd whatsapp-fastapi
```

2. **(Optional) Create virtual environment**

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. **Install requirements**

```bash
pip install -r requirements.txt
```

4. **Set Environment Variables**

```bash
export WHATSAPP_ACCESS_TOKEN="your-access-token"
export WHATSAPP_PHONE_NUMBER_ID="your-phone-number-id"
```

> Windows: use `set` instead of `export`

5. **Run the app**

```bash
uvicorn main:app --reload
```

6. **Test the Endpoint**

```
http://localhost:8000/send_message?phone_number=+1234567890
```

---

## 🛡️ Error Handling

- `400 Bad Request`: Invalid phone number format
- `500 Internal Server Error`: API/server issue