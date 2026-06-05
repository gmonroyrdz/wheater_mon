import requests, random, time

def generar_datos():
    return {
        "barrio": random.choice(["Centro", "Norte", "Sur"]),
        "temperatura": round(random.uniform(20, 40), 2),
        "humedad": round(random.uniform(30, 70), 2),
        "co2": round(random.uniform(300, 1000), 2)
    }

while True:
    data = generar_datos()
    try:
        requests.post("http://collector_service:5001/datos", json=data)
    except Exception as e:
        print("Error:", e)
    time.sleep(5)
