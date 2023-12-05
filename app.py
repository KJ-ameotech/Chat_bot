from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        text = request.json.get("message")
        if text is not None:
            response = get_response(text)
            message = {"answer": response}
            return jsonify(message)
        else:
            return jsonify({"error": "No 'message' found in request"})
    else:
        return jsonify({"error": "Unsupported method"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
