from flask import Blueprint, request,jsonify
from models import Platillo
from app import db

applatillo= Blueprint('applatillo',__name__,template_folder="templates")

@applatillo.route('/platillo/agregar',methods={'POST'})
def agregaPlatillo():
    try:
        json = request.get_json()
        platillo = Platillo()
        platillo.compañia = json['nombre']
        platillo.tamaño = json['descripcion']
        platillo.tipo = json['tamaño']
        db.session.add(platillo)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Platillo agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@applatillo.route('/platillo/editar',methods={"POST"})
def editaPlatillo():
    try:
        json = request.get_json()
        platillo = Platillo.query.get_or_404(json['id'])
        platillo.compañia = json['nombre']
        platillo.tamaño = json['descripcion']
        platillo.tipo = json['tamaño']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Platillo modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@applatillo.route('/platillo/eliminar',methods={"POST"})
def eliminaPlatillo():
    try:
        json = request.get_json()
        platillo = Platillo.query.get_or_404(json['id'])
        db.session.delete(platillo)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Platillo eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@applatillo.route('/platillo/obtener',methods={"GET"})
def obtenerPlatillo():
    platillos = Platillo.query.all()
    listaPlatillos=[]
    for p in platillos:
        platillo = {}
        platillo['nombre'] = p.nombre
        platillo['drescipcion'] = p.descripcion
        platillo['tamaño'] = p.tamaño
        listaPlatillos.append(platillo)
    return jsonify({'platillo':listaPlatillos})