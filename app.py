from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_reply
from flask_cors import CORS
import os

# Explicitly tell Flask where the templates folder is
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)

# ------------------ Routes ------------------ #
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    """
    Receives JSON { "message": "<user_input>" } from front-end
    Returns JSON { "reply": "<bot_reply>" }
    """
    try:
        data = request.get_json()
        user_input = data.get("message", "").strip()
        bot_reply = get_bot_reply(user_input)
        return jsonify({"reply": bot_reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error processing request: {str(e)}"})

# ------------------ Run Server ------------------ #
if __name__ == "__main__":
    # host="0.0.0.0" allows external access
    # port=5000 is default, you can change if needed
    app.run(debug=True, host="0.0.0.0", port=5000)
