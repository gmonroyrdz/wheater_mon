from flask import Flask, request, jsonify
from flasgger import Swagger
import requests

app = Flask(__name__)
Swagger(app)

@app.route("/datos", methods=["POST"])
def recibir_datos():
    """
    Recibe datos de sensores y los reenvía a otros servicios.
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            barrio:
              type: string
            temperatura:
              type: number
            humedad:
              type: number
            co2:
              type: number
    responses:
      200:
        description: Datos reenviados correctamente
    """
    data = request.get_json()
    try:
        requests.post("http://storage_service:5002/store", json=data)
        requests.post("http://alert_service:5003/alert", json=data)
    except Exception as e:
        print("Error:", e)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
