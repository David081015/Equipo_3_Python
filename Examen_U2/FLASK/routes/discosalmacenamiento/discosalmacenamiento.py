from flask import Blueprint, request,jsonify
from models import DiscoAlmacenamiento
from app import db

appdisco= Blueprint('appdisco',__name__,template_folder="templates")

@appdisco.route('/disco/agregar',methods={'POST'})
def agregaDisco():
    try:
        json = request.get_json()
        dicoalmacenamiento = DiscoAlmacenamiento()
        dicoalmacenamiento.compañia = json['compañia']
        dicoalmacenamiento.tamaño = json['tamaño']
        dicoalmacenamiento.tipo = json['tipo']
        db.session.add(dicoalmacenamiento)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Disco de almacenamiento agregado"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@appdisco.route('/disco/editar',methods={"POST"})
def editaDisco():
    try:
        json = request.get_json()
        dicoalmacenamiento = DiscoAlmacenamiento.query.get_or_404(json['id'])
        dicoalmacenamiento.compañia = json['compañia']
        dicoalmacenamiento.tamaño = json['tamaño']
        dicoalmacenamiento.tipo = json['tipo']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Disco de almacenamiento modificado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@appdisco.route('/disco/eliminar',methods={"POST"})
def eliminaDisco():
    try:
        json = request.get_json()
        discoalmacenamiento = DiscoAlmacenamiento.query.get_or_404(json['id'])
        db.session.delete(discoalmacenamiento)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Disco de almacenamiento eliminado"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@appdisco.route('/disco/obtener',methods={"GET"})
def obtenerDisco():
    discosalmacenamiento = DiscoAlmacenamiento.query.all()
    listaDiscoAlmacenamiento=[]
    for d in discosalmacenamiento:
        discoalmacenamiento = {}
        discoalmacenamiento['compañia'] = d.compañia
        discoalmacenamiento['tamaño'] = d.tamaño
        discoalmacenamiento['tipo'] = d.tipo
        listaDiscoAlmacenamiento.append(discoalmacenamiento)
    return jsonify({'disco':listaDiscoAlmacenamiento})