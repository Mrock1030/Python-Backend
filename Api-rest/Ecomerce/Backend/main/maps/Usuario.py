from marshmallow import Schema, fields, post_load, post_dump
from main.models import UsuarioModel

class UsuarioSchemas(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Stringing(required=True)
    apellido = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    rol = fields.String(required=True)
    telefono = fields.String(required=True)
    fecha_registro = fields.DateTime(required=False)


    @post_load
    def create_usuario(self, data, **kwargs):
        return UsuarioModel(**data)
    
    SKIP_VALUES =['password']
    
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if value not in self.SKIP_VALUES
        }





