from flask import Flask, render_template
# Imports:
# 1. Flask - used to create the Flask application
# 2. render_template - used to render an HTML template


app = Flask(__name__)
# Creates the Flask application


@app.route("/")
def home():
    posts = [
        {
            "title": "My Favorite Singer",
            "content": "KALEO is the GSOAT (greatest singer of all time)."
        },
        {
            "title": "This site is not made with JS.",
            "content": "This blog uses Python with the Flask library."
        }
    ]

    return render_template("index.html", posts=posts)
    # Sends the posts data to the Jinja template.
    # Jinja uses the data to generate the final HTML
    # before Flask sends the page to the browser.


# When a client makes an HTTP request to "/",
# Flask runs the home() function.


@app.route("/about")
def about():
    return "About Skuggi"
# When a client makes an HTTP request to "/about",
# Flask runs the about() function and returns the text above.


if __name__ == "__main__":
    app.run(debug=True)
# If this Python file is being run directly,
# start Flask's development server.
# debug=True automatically reloads the server when
# we make changes during development.
