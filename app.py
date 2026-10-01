from flask import Flask
# Imports Flask


app = Flask(__name__)
# creates the Flask app

@app.route("/")
def home():
    return "Hello, Skuggi!"
# When x makes a HTTP request to / run the homw fucntion

if __name__ == "__main__":
    app.run(debug=True)
# If i am running this python file directly,
# start the Flask development