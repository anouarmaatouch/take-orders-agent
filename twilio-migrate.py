import logging
from flask import Flask, request, Response

app = Flask(__name__)

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("twilio-webhook")

@app.route("/webhooks/answer", methods=["POST"])
def answer_call():
    # Twilio sends form-encoded data
    from_number = request.form.get("From")
    to_number = request.form.get("To")
    
    logger.info(f"Incoming call from {from_number} to {to_number}")

    # Respond with TwiML
    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">Hello! Your call from {from_number} is connected successfully.</Say>
</Response>"""
    
    return Response(twiml, mimetype="text/xml")


if __name__ == "__main__":
    # Run Flask server
    app.run(port=5000)
