from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
Swagger(app)

ultima_alerta = {}

#@app.route("/", methods=["GET"])
#def home():
#    return "Servicio de Alertas activo", 200

@app.route("/alert", methods=["POST"])
def alertar():
    """
    Recibe datos y verifica si se debe generar una alerta.
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
            co2:
              type: number
    responses:
      200:
        description: Verificación de alerta completada
    """
    global ultima_alerta
    data = request.get_json()
    ultima_alerta = data
    if data["temperatura"] > 35 or data["co2"] > 800:
        print("! ALERTA:", data)
    return {"status": "ok"}

@app.route("/alert", methods=["GET"])
def obtener_alerta():
    return jsonify(ultima_alerta),200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
