from flask import Blueprint, request,jsonify
from models import Refresco
from app import db

apprefresco= Blueprint('apprefresco',__name__,template_folder="templates")

@apprefresco.route('/refresco/agregar',methods={'POST'})
def agregaRefresco():
    try:
        json = request.get_json()
        refresco = Refresco()
        refresco.nombre = json['nombre']
        refresco.marca = json['marca']
        refresco.ml = json['ml']
        db.session.add(refresco)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"refresco agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@apprefresco.route('/refresco/editar',methods={"POST"})
def editaRefresco():
    try:
        json = request.get_json()
        refresco = Refresco.query.get_or_404(json['id'])
        refresco.nombre = json['nombre']
        refresco.marca = json['marca']
        refresco.ml = json['ml']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"refresco modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@apprefresco.route('/refresco/eliminar',methods={"POST"})
def eliminaRefresco():
    try:
        json = request.get_json()
        refresco = Refresco.query.get_or_404(json['id'])
        db.session.delete(refresco)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"refresco eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@apprefresco.route('/refresco/obtener',methods={"GET"})
def obtenerRefresco():
    refrescos = Refresco.query.all()
    listaRefrescos=[]
    for r in refrescos:
        refresco = {}
        refresco['nombre'] = r.nombre
        refresco['marca'] = r.marca
        refresco['ml'] = r.ml
        listaRefrescos.append(refresco)
    return jsonify({'refresco':listaRefrescos})