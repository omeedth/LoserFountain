from flask import Flask, request, send_from_directory, redirect
from twilio.twiml.messaging_response import MessagingResponse
from flask import render_template
import time
from threading import Thread
import random

phone_nums = []

app = Flask(__name__)

words = {}

# start = time.time()
# print(start)
elapsed = 0
wait = 30
thread = None

def get_time():
    elapsed = 0
    counter = 0
    timing = 0
    running = True
    start = time.time()
    while running:
        # start = time.time()
        elapsed += (time.time() - start)
        start = time.time()

        # if counter == 1:
        #     print("1 second")

        # if not url_ok(url):
        #     running = False
        #     break

        # if counter >= 3:
        #     running = False
        #     break

        if elapsed > 1:
            elapsed = 0
            counter += 1
            open("timer.txt","w").close()
            text = open("timer.txt","w")
            text.write(str(counter))
            text.close()
            # timing += 1
            print("Time: " + str(counter))
            # post_messages("timer",counter) # Timer Variable

        if counter >= wait:
            PopularWord = getPopularWord()
            # post_messages("PopularWord",PopularWord) # Posts Chosen Word
            if PopularWord != "":
                print("Most popular word: " + PopularWord)
                text = open("madlib.txt","a")
                text.write(PopularWord + " ")
                text.close()
            elapsed = 0
            words.clear()
            print("Cleared Dictionary: " + str(words))
            phone_nums.clear()
            counter += 1

            votes = open("votes.txt","r")
            contents = votes.read()
            tokens = contents.split(",")[:-1]
            votes.close()

            # post_messages("votes",tokens) # Posts Chosen Word

            print("Voted Words: " + str(tokens))

            votes = open("votes.txt","w")
            votes.write("")
            votes.close()

            counter = 0
            # timing = 0
    # thread.join();
    # quit()

def getPopularWord():
    max = 0
    ret = ""
    tied = []
    for key,val in words.items():
        if val >= max:
            max = val
        print(str(key) + ":" + str(val),end="")
    for key,val in words.items():
        if val == max:
            tied.append(key)
    ret = random.choice(tied)
    print()
    return ret

@app.route("/twilio", methods=["GET", "POST"])
def replyRead():
    """Respond to incoming messages with a friendly SMS."""

    # phone_nums = []

    print("twilio method called...")

    resp = MessagingResponse()

    if resp is None:
        return ""

    fromNumber = request.values.get("From", None)
    fromMessage = request.values.get("Body", None);

    # numbers = open("nums.txt","a")
    # numbers.write(fromNumber)
    # numbers.close()

    # phone_nums = numbers.split(" ")

    if fromNumber in phone_nums:
        print(phone_nums)
        return ""

    phone_nums.append(fromNumber)

    fromMessage = str(fromMessage).split(" ")[0].lower()

    votes = open("votes.txt","a")
    votes.write(fromMessage + ",")
    votes.close()

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

    return ""
    # return str(resp)

@app.route("/madlib.txt")
def post_madlib():
    return send_from_directory('','madlib.txt')

@app.route("/votes.txt")
def post_votes():
    return send_from_directory('','votes.txt')

@app.route("/timer.txt")
def post_timer():
    return send_from_directory('','timer.txt')

# @app.route("/send",methods=["POST"])
# def post_messages(key,val):
#     if request.method == 'POST':
#         if(key == "counter"):
#             return render_template("flask.html",timer=val)
#         elif(key == "PopularWord"):
#             return render_template("flask.html",word=val)
#         elif(key == "votes"):
#             return render_template("flask.html",votes=val)
        # return render_template("flask.html")

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
