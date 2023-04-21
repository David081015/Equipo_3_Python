from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PlatilloForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    descripcion = StringField('Descripcion',validators=[DataRequired()])
    tamaño = StringField('Tamaño',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class RefrescoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    marca = StringField('Marca',validators=[DataRequired()])
    ml = StringField('Ml',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')

class DiscoAlmacenamientoForm(FlaskForm):
    compañia = StringField('Compañia',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    tamaño = StringField('Tamaño',validators=[DataRequired()])
    tipo = StringField('Tipo',validators=[DataRequired()])
    enviar =  SubmitField('Enviar')

class LaptopForm(FlaskForm):
    marca = StringField('Marca',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    procesador = StringField('Procesador',validators=[DataRequired()])
    precio = StringField('Precio',validators=[DataRequired()])
    enviar =  SubmitField('Enviar')

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    apellido = StringField('Apellido',validators=[DataRequired()])
    promedio = StringField('Promedio',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')
