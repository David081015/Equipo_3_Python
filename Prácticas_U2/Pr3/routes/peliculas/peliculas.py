from flask import Blueprint, request, render_template, redirect,url_for, jsonify
from models import Pelicula
from forms import PeliculaForm
from app import db

appelicula = Blueprint('appelicula',__name__,template_folder="templates")
apphttp = Blueprint('apphttp',__name__,template_folder="templates")

@appelicula.route('/indexPelicula')
def inicio():
    peliculas = Pelicula.query.all()
    totalDePeliculas = Pelicula.query.count()
    return render_template('indexPelicula.html',peliculas =peliculas, totalDePeliculas = totalDePeliculas)

@appelicula.route('/agregarPelicula',methods=["GET","POST"])
def agregar():
    pelicula = Pelicula()
    peliculaForm = PeliculaForm(obj=pelicula)
    if request.method == "POST":
        if peliculaForm.validate_on_submit():
            peliculaForm.populate_obj(pelicula)
            db.session.add(pelicula)
            db.session.commit()
            return redirect(url_for('appelicula.inicio'))
    return render_template('agregarPelicula.html',forma=peliculaForm)

@appelicula.route('/editarPelicula/<int:id>',methods=["GET","POST"])
def editar(id):
    pelicula = Pelicula.query.get_or_404(id)
    peliculaForm = PeliculaForm(obj=pelicula)
    if request.method == "POST":
        if peliculaForm.validate_on_submit():
            peliculaForm.populate_obj(pelicula)
            db.session.commit()
            return redirect(url_for('appelicula.inicio'))
    return render_template('editarPelicula.html',forma=peliculaForm)

@appelicula.route('/detallePelicula/<int:id>')
def detalle(id):
    pelicula = Pelicula.query.get_or_404(id)
    return render_template('detallePelicula.html',pelicula = pelicula)

@appelicula.route('/eliminarPelicula/<int:id>')
def eliminar(id):
    pelicula = Pelicula.query.get_or_404(id)
    db.session.delete(pelicula)
    db.session.commit()
    return redirect(url_for('appelicula.inicio'))


#------------------HTTP
@apphttp.route('/pelicula/agregar',methods={'POST'})
def agregarPelicula():
    try:
        json = request.get_json()
        pelicula = Pelicula()
        pelicula.nombre = json['nombre']
        pelicula.duracion = json['duracion']
        pelicula.categoria = json['categoria']
        db.session.add(pelicula)
        db.session.commit()
        return jsonify({"status":200, "mensaje":"Pelicula agregada"})
    except Exception as ex:
        return jsonify({"status":400,"mensaje":ex})

@apphttp.route('/pelicula/editar',methods={"POST"})
def editarPelicula():
    try:
        json = request.get_json()
        pelicula = Pelicula.query.get_or_404(json['id'])
        pelicula.nombre = json['nombre']
        pelicula.duracion = json['duracion']
        pelicula.categoria = json['categoria']
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Pelicula modificada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})
    
@apphttp.route('/pelicula/eliminar',methods={"POST"})
def eliminarPelicula():
    try:
        json = request.get_json()
        pelicula = Pelicula.query.get_or_404(json['id'])
        db.session.delete(pelicula)
        db.session.commit()
        return jsonify({'status':"OK",'mensaje':"Pelicula eliminada"})
    except Exception as ex:
        return jsonify({"status":"ERROR","mensaje":ex})

@apphttp.route('/pelicula/obtener',methods={"GET"})
def obtenerPelicula():
    peliculas = Pelicula.query.all()
    listaPeliculas=[]
    for p in peliculas:
        pelicula = {}
        pelicula['nombre'] = p.nombre
        pelicula['duracion'] = p.duracion
        pelicula['categoria'] = p.categoria
        listaPeliculas.append(pelicula)
    return jsonify({'peliculas':listaPeliculas})