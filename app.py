
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {
        "title": "Welcome to Skuggi",
        "content": "This is my first blog post."
    }
]


@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/create-post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["description"]

        posts.append({
            "title": title,
            "content": content
        })

        return redirect(url_for("index"))

    return render_template("post.html")


@app.route("/about")
def about():
    return "About Skuggi"


if __name__ == "__main__":
    app.run(debug=True)
