from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class VideojuegoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    plataforma = StringField('Plataforma',validators=[DataRequired()])
    empresa = StringField('Empresa',validators=[DataRequired()]) 
    precio = StringField('Precio',validators=[DataRequired()])
    enviar =  SubmitField('Enviar')

class PeliculaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    duracion = StringField('Duracion',validators=[DataRequired()])
    categoria = StringField('Categoria',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')
