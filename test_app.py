import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Iris Species Predictor" in response.data


def test_api_predict_valid_input(client):
    response = client.post(
        "/api/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["predicted_species"] in [
        "setosa",
        "versicolor",
        "virginica"
    ]

    assert 0.0 <= data["confidence"] <= 1.0


def test_api_predict_missing_field(client):
    response = client.post(
        "/api/predict",
        json={
            "sepal_length": 5.1
        }
    )

    assert response.status_code == 400


def test_api_predict_non_numeric_input(client):
    response = client.post(
        "/api/predict",
        json={
            "sepal_length": "abc",
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )

    assert response.status_code == 400