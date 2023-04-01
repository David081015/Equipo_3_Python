from flask import Blueprint, request, render_template, redirect,url_for
from models import Videojuego
from forms import VideojuegoForm
from app import db

appvideojuego = Blueprint('appvideojuego',__name__,template_folder="templates")

@appvideojuego.route('/index')
def inicio():
    videojuegos = Videojuego.query.all()
    totalDeVideojuegos = Videojuego.query.count()
    return render_template('index.html',videojuegos = videojuegos, totalDeVideojuegos = totalDeVideojuegos)

@appvideojuego.route('/agregar',methods=["GET","POST"])
def agregar():
    videojuego = Videojuego()
    videojuegoForm = VideojuegoForm(obj=videojuego)
    if request.method == "POST":
        if videojuegoForm.validate_on_submit():
            videojuegoForm.populate_obj(videojuego)
            db.session.add(videojuego)
            db.session.commit()
            return redirect(url_for('appvideojuego.inicio'))
    return render_template('agregar.html',forma=videojuegoForm)

@appvideojuego.route('/editar/<int:id>',methods=["GET","POST"])
def editar(id):
    videojuego = Videojuego.query.get_or_404(id)
    videojuegoForm = VideojuegoForm(obj=videojuego)
    if request.method == "POST":
        if videojuegoForm.validate_on_submit():
            videojuegoForm.populate_obj(videojuego)
            db.session.commit()
            return redirect(url_for('appvideojuego.inicio'))
    return render_template('editar.html',forma=videojuegoForm)

@appvideojuego.route('/detalle/<int:id>')
def detalle(id):
    videojuego = Videojuego.query.get_or_404(id)
    return render_template('detalle.html',videojuego = videojuego)

@appvideojuego.route('/eliminar/<int:id>')
def eliminar(id):
    videojuego = Videojuego.query.get_or_404(id)
    db.session.delete(videojuego)
    db.session.commit()
    return redirect(url_for('appvideojuego.inicio'))