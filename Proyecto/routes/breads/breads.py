from flask import Blueprint, request, render_template, redirect,url_for
from models import Pan
from forms import PanForm
from app import db

appbread = Blueprint('appbread',__name__,template_folder="templates")

@appbread.route('/listapanes')
def inicio():
    panes = Pan.query.all()
    totalDePanes = Pan.query.count()
    return render_template('index.html',panes = panes, totalDePanes = totalDePanes)

@appbread.route('/agregarpan',methods=["GET","POST"])
def agregar():
    pan = Pan()
    panForm = PanForm(obj=pan)
    if request.method == "POST":
        if panForm.validate_on_submit():
            panForm.populate_obj(pan)
            db.session.add(pan)
            db.session.commit()
            return redirect(url_for('appbread.inicio'))
    return render_template('agregar.html',forma=panForm)

@appbread.route('/editarpan/<int:id>',methods=["GET","POST"])
def editar(id):
    pan = Pan.query.get_or_404(id)
    panForm = PanForm(obj=pan)
    if request.method == "POST":
        if panForm.validate_on_submit():
            panForm.populate_obj(pan)
            db.session.commit()
            return redirect(url_for('appbread.inicio'))
    return render_template('editar.html',forma=panForm)

@appbread.route('/eliminarpan/<int:id>')
def eliminar(id):
    pan = Pan.query.get_or_404(id)
    db.session.delete(pan)
    db.session.commit()
    return redirect(url_for('appbread.inicio'))