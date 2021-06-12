from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

# Health-check endpoint
@app.route("/status")
def healthCheck():
    response = {
        "result": "OK - healthy"
    }
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )

# Metrics endpoint
@app.route("/metrics")
def metrics():
    response = {
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
