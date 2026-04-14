from flask import Flask, request

app = Flask(__name__)

@app.route("/metric", methods=["POST"])
def metric():
    print("Métrica recibida:", request.json)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
