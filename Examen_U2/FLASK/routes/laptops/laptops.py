from flask import Blueprint, request,jsonify
from models import Laptop
from app import db

applaptop= Blueprint('applaptop',__name__,template_folder="templates")

@applaptop.route('/laptop/agregar',methods={'POST'})
def agregaLaptop():
    try:
        json = request.get_json()
        laptop = Laptop()
        laptop.compañia = json['marca']
        laptop.tamaño = json['procesador']
        laptop.tipo = json['precio']
        db.session.add(laptop)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Laptop agregada"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@applaptop.route('/laptop/editar',methods={"POST"})
def editaLaptop():
    try:
        json = request.get_json()
        laptop= Laptop.query.get_or_404(json['id'])
        laptop.compañia = json['marca']
        laptop.tamaño = json['procesador']
        laptop.tipo = json['precio']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Laptop modificada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@applaptop.route('/laptop/eliminar',methods={"POST"})
def eliminaLaptop():
    try:
        json = request.get_json()
        laptop = Laptop.query.get_or_404(json['id'])
        db.session.delete(laptop)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Laptop eliminada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@applaptop.route('/laptop/obtener',methods={"GET"})
def obtenerLaptop():
    laptops = Laptop.query.all()
    listaLaptops=[]
    for l in laptops:
        laptop = {}
        laptop['compañia'] = l.marca
        laptop['tamaño'] = l.procesador
        laptop['tipo'] = l.precio
        listaLaptops.append(laptop)
    return jsonify({'laptop':listaLaptops})