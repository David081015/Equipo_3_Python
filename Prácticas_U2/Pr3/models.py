from app import db

class Videojuego(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    plataforma = db.Column(db.String(255))
    empresa= db.Column(db.String(255))
    precio = db.Column(db.String(255))

class Pelicula(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    duracion = db.Column(db.String(255))
    categoria= db.Column(db.String(255))

class Equipofut(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(255))
    color = db.Column(db.String(255))
    cantidadjugadores = db.Column(db.String(255))