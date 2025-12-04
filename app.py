from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"message": "Hello from deploy-test Flask app"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    # Development server for local tests
    app.run(host="0.0.0.0", port=8080, debug=True)
