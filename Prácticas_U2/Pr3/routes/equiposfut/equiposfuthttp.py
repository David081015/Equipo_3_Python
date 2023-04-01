from flask import Blueprint, request,jsonify
from models import Equipofut
from app import db

appequipofuthttp= Blueprint('appequipofuthttp',__name__,template_folder="templates")

@appequipofuthttp.route('/equipofut/agregar',methods={'POST'})
def agregaEquipofut():
    try:
        json = request.get_json()
        equipofut = Equipofut()
        equipofut.nombre = json['nombre']
        equipofut.color = json['color']
        equipofut.cantidadjugadores = json['cantidadjugadores']
        db.session.add(equipofut)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Equipofut agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appequipofuthttp.route('/equipofut/editar',methods={"POST"})
def editaEquipofut():
    try:
        json = request.get_json()
        equipofut = Equipofut.query.get_or_404(json['id'])
        equipofut.nombre = json['nombre']
        equipofut.color = json['color']
        equipofut.cantidadjugadores = json['cantidadjugadores']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Equipofut modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appequipofuthttp.route('/equipofut/eliminar',methods={"POST"})
def eliminaEquipofut():
    try:
        json = request.get_json()
        equipofut = Equipofut.query.get_or_404(json['id'])
        db.session.delete(equipofut)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Equipofut eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appequipofuthttp.route('/equipofut/obtener',methods={"GET"})
def obtenerEquipofut():
    equiposfut = Equipofut.query.all()
    listaEquiposfut=[]
    for e in equiposfut:
        equipofut = {}
        equipofut['nombre'] = e.nombre
        equipofut['color'] = e.color
        equipofut['cantidadjugadores'] = e.cantidadjugadores
        listaEquiposfut.append(equipofut)
    return jsonify({'equiposfut':listaEquiposfut})