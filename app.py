from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chatbot import get_bot_reply
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Explicitly tell Flask where the templates folder is
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
app = Flask(__name__, template_folder=template_dir)

# Allow all origins for debugging; restrict in production
CORS(app, resources={r"/get": {"origins": "*"}})

# ------------------ Routes ------------------ #
@app.route("/")
def index():
    app.logger.debug("Serving index.html")
    return render_template("index.html")

@app.route("/test")
def test():
    app.logger.debug("Test endpoint accessed")
    return jsonify({"status": "Server is running"})

@app.route("/get", methods=["POST"])
def chat():
    """
    Receives JSON { "message": "<user_input>" } from front-end
    Returns JSON { "reply": "<bot_reply>" }
    """
    app.logger.debug(f"Received POST /get request. Origin: {request.headers.get('Origin')}, Headers: {request.headers}, Data: {request.get_data(as_text=True)}")
    try:
        data = request.get_json()
        app.logger.debug(f"Parsed JSON: {data}")
        user_input = data.get("message", "").strip()
        if not user_input:
            app.logger.warning("No message provided in request")
            return jsonify({"reply": "⚠️ No message provided."}), 400
        
        bot_reply = get_bot_reply(user_input)
        app.logger.debug(f"Bot reply: {bot_reply}")
        return jsonify({"reply": bot_reply})
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"reply": f"⚠️ Server error: {str(e)}"}), 500

# ------------------ Run Server ------------------ #
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)