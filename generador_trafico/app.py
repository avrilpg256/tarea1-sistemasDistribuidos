import requests
import time
import random

while True:
    query = {
        "type": random.choice(["Q1", "Q2", "Q3", "Q4", "Q5"]),
        "zone": random.choice(["Z1", "Z2", "Z3", "Z4", "Z5"])
    }

    try:
        res = requests.post(
            "http://response-generator:5000/query",
            json=query
        )
        print("Respuesta:", res.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(2)
