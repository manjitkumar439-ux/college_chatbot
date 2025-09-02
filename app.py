from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_bot_reply_fixed as get_bot_reply

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    bot_reply = get_bot_reply(user_input)
    return jsonify({"reply": bot_reply})

# Important for Render
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
