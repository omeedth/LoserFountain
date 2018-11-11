from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask import render_template
import time
from threading import Thread

app = Flask(__name__)

words = {}
# start = time.time()
# print(start)
elapsed = 0
wait = 5
thread = None

def getPopularWord():
    for i in len(words):
        #print(pair,end="")
    print()
    return ""

def get_time():
    elapsed = 0
    # counter = 0
    running = True
    while running:
        start = time.time()
        elapsed += (time.time() - start)
        start = time.time()
        # if counter % 1000:
        #     print("Time: " + str(elapsed))
        if elapsed > wait:
            text = open("madlib.txt","w")
            text.write(getPopularWord())
            text.close()
            elapsed = 0
            words.clear()
            print("Cleared Dictionary: " + str(words))
        # counter += 1

    thread.join()

@app.route("/twilio", methods=["GET", "POST"])
def replyRead():
    """Respond to incoming messages with a friendly SMS."""

    print("twilio method called...")

    resp = MessagingResponse()

    if resp is None:
        return ""

    fromNumber = request.values.get("From", None)
    fromMessage = request.values.get("Body", None);

    fromMessage = fromMessage.lower()

    # Works
    # text = open("madlib.txt","w")
    # text.write(fromMessage)
    # text.close()

    # Add a message
    resp.message(fromMessage)

    # Add to database
    if fromMessage in words:
        words[fromMessage] += 1
    else:
        words[fromMessage] = 1

    print(words)

    return str(resp)

@app.route("/", methods=["GET"])
def run_site():
    msg = "hey"
    print("start...")
    thread = Thread(target = get_time)
    thread.start()
    # get_time()
    #fromMessage = request.args.get('fromMessage', None)
    return render_template('flask.html',msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
