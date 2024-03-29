from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PanForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()]) #Validators hace obligatorio el campo 
    precio = StringField('Precio',validators=[DataRequired()])
    cantidad = StringField('Cantidad',validators=[DataRequired()]) 
    enviar =  SubmitField('Enviar',render_kw={'class': 'submit-button'})