from flask import Flask
app = Flask(__name__)

@app.route("/")
def goodbye():
    return "Hello World..."
def hello():
    return "Goodbye World..."

if __name__ == "__main__":
    app.run(debug=True)
