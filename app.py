from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_reply
import os

# Explicitly tell Flask where the templates folder is
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    bot_reply = get_bot_reply(user_input)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

