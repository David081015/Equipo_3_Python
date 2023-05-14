from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PanFormForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    precio = StringField('Precio',validators=[DataRequired()])
    cantidad = StringField('Cantidad',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar')