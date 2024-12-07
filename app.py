from flask import Flask, render_template
import random

app = Flask(__name__)

# List of quotes
quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "You only live once, but if you do it right, once is enough. – Mae West",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "In the middle of every difficulty lies opportunity. – Albert Einstein"
]

@app.route("/")
def index():
    quote = random.choice(quotes)  # Pick a random quote
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
