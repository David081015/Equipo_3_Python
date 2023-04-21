from app import db

class Platillo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    descripcion = db.Column(db.String(255))
    tamaño = db.Column(db.String(255))

class Refresco(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    marca = db.Column(db.String(255))
    ml = db.Column(db.String(255))

class DiscoAlmacenamiento(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    compañia = db.Column(db.String(255))
    tamaño = db.Column(db.String(255))
    tipo = db.Column(db.String(255))

class Laptop(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    marca = db.Column(db.String(255))
    procesador = db.Column(db.String(255))
    precio = db.Column(db.String(255))

class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    apellido = db.Column(db.String(255))
    promedio = db.Column(db.String(255))