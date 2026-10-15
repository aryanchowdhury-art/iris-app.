from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
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

    required_fields = [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]

    # Check for missing fields
    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"Missing required field: {field}"
            }), 400

    # Check for non-numeric values
    try:
        sepal_length = float(data["sepal_length"])
        sepal_width = float(data["sepal_width"])
        petal_length = float(data["petal_length"])
        petal_width = float(data["petal_width"])
    except (ValueError, TypeError):
        return jsonify({
            "error": "All inputs must be numeric"
        }), 400

    # Simple prediction logic
    if petal_length < 2:
        predicted_species = "setosa"
        confidence = 0.98
    elif petal_length < 5:
        predicted_species = "versicolor"
        confidence = 0.92
    else:
        predicted_species = "virginica"
        confidence = 0.95

    return jsonify({
        "predicted_species": predicted_species,
        "confidence": confidence
    })


if __name__ == "__main__":
    app.run(debug=True)