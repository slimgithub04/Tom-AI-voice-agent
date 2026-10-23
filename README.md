# Outbound Call Tool (FastAPI + VAPI)

A small FastAPI web application that triggers outbound voice calls via the **VAPI.ai** API using a preconfigured assistant.

The web UI lets you enter a phone number and hit a button to initiate a call. In this sample implementation, the call payload is hard-coded (symbol, price, score, reason, risk level), but the project can be extended to generate dynamic call content based on user input or business logic.

---

## 🚀 Features

- FastAPI backend with a simple web UI
- Sends a POST request to `https://api.vapi.ai/call` to start a voice call
- Uses Jinja2 templates for the frontend
- Uses `requests` to communicate with VAPI

---

## 🧩 Project Structure

- `main.py` – FastAPI app and call-triggering logic
- `templates/index.html` – Frontend UI (phone number input + button)
- `static/` – Static assets (currently unused but mounted by FastAPI)
- `requirements.txt` – Python dependencies

---

## ✅ Prerequisites

- Python 3.10+ (recommended)
- A VAPI.ai account and valid API key
- A VAPI assistant ID, phone number ID, and a target phone number

---

## 🛠️ Setup

1. Create a Python virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment:

- **Windows (PowerShell):**
  ```powershell
  .\.venv\Scripts\Activate.ps1
  ```
- **Windows (cmd):**
  ```cmd
  .\.venv\Scripts\activate.bat
  ```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) Create a `.env` file to store credentials locally.

Create a file named `.env` next to `main.py` with the following values:

```env
VAPI_API_KEY=<your_api_key>
VAPI_ASSISTANT_ID=<your_assistant_id>
VAPI_PHONE_NUMBER_ID=<your_phone_number_id>
USER_PHONE_NUMBER=+1234567890
```

> **NOTE:** `main.py` reads these values from the environment (or from `.env` via `python-dotenv`). Never commit real keys.

You can set your environment variables like this (PowerShell example):

```powershell
$env:VAPI_API_KEY = "<your_api_key>"
$env:VAPI_ASSISTANT_ID = "<your_assistant_id>"
$env:VAPI_PHONE_NUMBER_ID = "<your_phone_number_id>"
$env:USER_PHONE_NUMBER = "+1234567890"
```


---

## ▶️ Run the app

Start the FastAPI server:

```bash
python main.py
```

Open your browser at:

```
http://127.0.0.1:8000/
```

Enter a phone number and click **Make Outbound Call**.

---

## 🔧 Customizing the Call Payload

The call content is currently defined in `main.py` inside the `make_call()` handler:

```python
symbol = "SOL"
price = 145.50
score = 95
reason = "Solana has huge momentum. This is a real test."
risk_level = "High"
```

You can replace these values with dynamic values from the request body, database, or any business logic.

---

## 🧪 Example API Usage (curl)

```bash
curl -X POST "http://127.0.0.1:8000/call" \
  -H "Content-Type: application/json" \
  -d '{"phoneNumber": "+1234567890"}'
```

---

## ✅ Improvements / Next Steps

- Store secrets securely (environment variables, vault, etc.)
- Add validation for phone numbers
- Add more user inputs (call content, variables) for dynamic calls
- Add error handling / logging for API responses

---

## 📄 License

This project is provided as-is with no license. Add a `LICENSE` file if you plan to share or distribute it.
