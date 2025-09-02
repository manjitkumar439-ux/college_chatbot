from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_bot_reply_fixed as get_bot_reply
import os

# Create Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend JS to access API

# Route for main page
@app.route("/")
def index():
    return render_template("index.html")

# Route for chatbot API
@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")  # Match frontend key
    bot_reply = get_bot_reply(user_input)
    return jsonify({"reply": bot_reply})

# Run app
if __name__ == "__main__":
    # Use Render-assigned port if deployed, otherwise default 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

