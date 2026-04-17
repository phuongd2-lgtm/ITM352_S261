from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://meme-api.com/gimme/wholesomememes"
    
    response = requests.get(url)
    data = response.json()

    meme_url = data["url"]
    subreddit = data["subreddit"]

    return render_template("index.html", meme_url=meme_url, subreddit=subreddit)

if __name__ == "__main__":
    app.run(debug=True)