from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

data_store = []

@app.route("/store", methods=["POST"])
def almacenar():
    """
    Almacena datos enviados por sensores.
    ---
    parameters:
      - in: body
        name: data
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
        description: Datos almacenados correctamente
    """
    data = request.get_json()
    data_store.append(data)
    return {"status": "almacenado"}

@app.route("/datos", methods=["GET"])
def obtener():
    """
    Consulta los últimos datos almacenados.
    ---
    responses:
      200:
        description: Lista de últimos datos
    """
    return jsonify(data_store[-10:])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
