from flask_restful import Resource
#importamos jsonify para devolver todo en tipo json
from flask import jsonify, request


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
    ##agregamos otro cliente
    def post(self):
        cliente = request.get_json()
        print(cliente)
        clientes.append(cliente)
        return cliente, 201


class Cliente (Resource):

    def get(self,id):
        return jsonify(
            {
            "clientes":clientes[int(id)-1]
            }
            )