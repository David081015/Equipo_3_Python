from flask import Blueprint, request, render_template, redirect,url_for
from models import Alumno
from forms import AlumnoForm
from app import db

appalumno = Blueprint('appalumno',__name__,template_folder="templates")

@appalumno.route('/indexAlumno')
def inicio():
    alumnos = Alumno.query.all()
    totalDeAlumnos = Alumno.query.count()
    return render_template('indexAlumno.html',alumnos =alumnos, totalDeAlumnos = totalDeAlumnos)

@appalumno.route('/agregarAlumno',methods=["GET","POST"])
def agregar():
    alumno = Alumno()
    alumnoForm = AlumnoForm(obj=alumno)
    if request.method == "POST":
        if alumnoForm.validate_on_submit():
            alumnoForm.populate_obj(alumno)
            db.session.add(alumno)
            db.session.commit()
            return redirect(url_for('appalumno.inicio'))
    return render_template('agregarAlumno.html',forma=alumnoForm)

@appalumno.route('/editarAlumno/<int:id>',methods=["GET","POST"])
def editar(id):
    alumno = Alumno.query.get_or_404(id)
    alumnoForm = AlumnoForm(obj=alumno)
    if request.method == "POST":
        if alumnoForm.validate_on_submit():
            alumnoForm.populate_obj(alumno)
            db.session.commit()
            return redirect(url_for('appalumno.inicio'))
    return render_template('editarAlumno.html',forma=alumnoForm)

@appalumno.route('/detalleAlumno/<int:id>')
def detalle(id):
    alumno = Alumno.query.get_or_404(id)
    return render_template('detalleAlumno.html',alumno = alumno)

@appalumno.route('/eliminarAlumno/<int:id>')
def eliminar(id):
    alumno= Alumno.query.get_or_404(id)
    db.session.delete(alumno)
    db.session.commit()
    return redirect(url_for('appalumno.inicio'))