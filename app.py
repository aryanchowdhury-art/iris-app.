from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Iris Species Predictor</title>
        </head>
        <body>
            <h1>Iris Species Predictor</h1>
        </body>
    </html>
    """


@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()

    return jsonify({
        "predicted_species": "setosa",
        "confidence": 0.95
    })


if __name__ == "__main__":
    app.run(debug=True)