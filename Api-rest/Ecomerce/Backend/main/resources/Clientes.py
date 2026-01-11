from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify

clientes = [
    {
        "id":1,
        "nombre":"Juan",
        "apellido":"Martinez"
    },
    {
        "id":2,
        "nombre":"Pedro",
        "apellido":"Martinez"
    }
]

#### creamos la clase clientes###

class Clientes (Resource):

    def get(self):
        return jsonify(
            {
            "clientes":clientes
            }
            )