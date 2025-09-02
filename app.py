from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_reply_fixed as get_bot_reply

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")   # match frontend key
    bot_reply = get_bot_reply(user_input)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
