from flask import Flask, jsonify, request
from embed import get_text_embeddings

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"name": "llama-index-api"})


@app.route("/embedding", methods=["POST"])
def embedding():
    data = request.get_json()
    text_list = data.get("text", [])
    if len(text_list) == 0:
        return jsonify({"error": "no text provided"}), 400

    embeddings = get_text_embeddings(text_list)
    return jsonify({"embeddings": embeddings})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
