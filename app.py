from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""

    running = True

    # Display website
    run_site()

    while running:
        wait_for_message()


if __name__ == "__main__":
    app.run(debug=True)

def run_site():
    return render_template('flask.html')

def wait_for_message():
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Alex is a dummy boy.")

    return str(resp)
