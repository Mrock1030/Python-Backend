from .. import db
from main.models import CompraModel

class CompraRepository:
    __model = CompraModel
    
    @property 
    def model(self):
        return self.__model
    
    def find_one(self, id):
        object = db.session.query(self.model).get(id)
        return object
    
    def find_all(self):
        objects = db.session.query(self.model).all()
        return objects
    
    def create(self, object):
        db.session.add(object)
        db.session.commit()
        return object
    
    def update(self, object):
        return self.create(object)
    
    def delete(self, object):
        object= self.find_one(id)
        db.session.delete(object)
        db.session.commit()
        return object

    