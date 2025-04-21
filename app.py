from flask import Flask, render_template
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "Long drive without any destination.",
    "To the mountains and never back.",
    "You only live once, but if you do it right, once is enough.",
    "Do what you can, with what you have, where you are.",
    "In the middle of every difficulty lies opportunity.",
    "Life is too short bro. Pack your bags and explore!!",
    "Somewhere between the dream and destination."
]

@app.route("/")
def index():
    quote = random.choice(quotes)  # Pick a random quote
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
