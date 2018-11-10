from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask import render_template

app = Flask(__name__)

@app.route("/twilio", methods=["GET", "POST"])

def replyRead():
    """Respond to incoming messages with a friendly SMS."""

    resp = MessagingResponse()
    fromNumber = request.values.get("From", None)
    fromMessage = request.values.get("Body", None);

    # Add a message
    resp.message(fromMessage)

    return str(resp)

@app.route("/")

def run_site():
    return render_template('flask.html')

if __name__ == "__main__":
    app.run(debug=True)
