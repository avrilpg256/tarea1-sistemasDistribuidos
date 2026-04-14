from flask import Flask, request, jsonify
import time
import random

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query():
    data = request.json

    # Simula procesamiento
    time.sleep(random.uniform(0.05, 0.2))

    return jsonify({
        "status": "ok",
        "query": data,
        "result": random.randint(1, 100)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
