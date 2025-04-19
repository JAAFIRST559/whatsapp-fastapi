# ** Hey There, I'm Jasmine Ilakkia Neviskennedy, and I've Developed the WhatsApp Messaging via FastAPI Project**
- In this project, I’ve built a FastAPI application that integrates with Meta’s WhatsApp Business Manager API to send WhatsApp messages programmatically. The core objective was to expose an endpoint (/send_message) that allows users to send a predefined message ("Hello, this is a test message from our TMBC bot!") to a specified phone number.
- What I've Done:
Phone Number Validation: I implemented a phone number validation feature that ensures the number is in the correct E.164 format (e.g., +1234567890), preventing errors or bad data from being processed.

WhatsApp Message Integration: I integrated with Meta’s WhatsApp Business API to send messages via HTTP requests, utilizing the API's authentication mechanisms.

Error Handling & Logging: I built robust error handling to handle invalid phone numbers and potential API failures, ensuring the user gets clear feedback. Additionally, I incorporated logging to track and debug the flow of the application effectively.

Asynchronous Request Handling: I used httpx, an asynchronous HTTP client, to interact with the WhatsApp API efficiently.

# WhatsApp Messaging via FastAPI

This FastAPI app sends WhatsApp messages using Meta's WhatsApp Business API.

## 🚀 Features

- Endpoint: `/send_message`
- Message: `"Hello, this is a test message from our TMBC bot!"`
- Accepts phone number as a query parameter in E.164 format (e.g., +1234567890)
- Includes phone number validation and error handling

## 🧰 Tech Stack

- Python
- FastAPI: I chose FastAPI due to its speed and simplicity in building modern, fast APIs.
- Meta WhatsApp Cloud API: This project uses the official WhatsApp Cloud API to send messages.
- httpx: For making asynchronous requests to the WhatsApp API.
- Logging: To capture critical events and ensure visibility into the app's operation.

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

## Why I Built This Project:
- I wanted to explore API development, integrate with external services, and ensure proper handling of different scenarios such as invalid inputs and API issues. This project is useful for building automated messaging systems and chatbots using WhatsApp, a platform that many businesses rely on for communication.

- Feel free to check out the code, run the app locally, and test the message sending functionality! If you have any questions or suggestions, feel free to reach out.

