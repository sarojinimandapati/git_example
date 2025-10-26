from flask import Flask
import os

app=Flask(__name__)

@app.route("/")
def index():
    return "This is my first render upload"


if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's port
    app.run(host="0.0.0.0", port=port)
