from flask import Flask, jsonify, request
from embed import get_text_embedding

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"name": "llama-index-api"})


@app.route("/embedding", methods=["POST"])
def embedding():
    data = request.get_json()
    text = str(data.get("text", ""))
    if not text:
        return jsonify({"error": "text is required"}), 400

    embedding = get_text_embedding(text)
    return jsonify({"embedding": embedding})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
