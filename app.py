from flask import Flask, render_template, request, jsonify
from chatbot import generate_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    reply = generate_response(message)
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)