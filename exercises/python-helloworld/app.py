from flask import Flask, json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    app.logger.info("'/' endpoint was reached")
    return app.response_class(
        response=json.dumps({"message": "Hello World!"}),
        status=200,
        mimetype='application/json'
    )

# Health-check endpoint
@app.route("/status")
def healthCheck():
    response = {
        "result": "OK - healthy"
    }
    app.logger.info("'/status' endpoint was reached")
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
    app.logger.info("'/metrics' endpoint was reached")
    return app.response_class(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":

    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')
