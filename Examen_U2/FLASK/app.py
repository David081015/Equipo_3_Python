from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig
#Routes
from routes.alumnos.alumnos import appalumno
from routes.discosalmacenamiento.discosalmacenamiento import appdisco
from routes.errores.errores import apperror
from routes.laptops.laptops import applaptop
from routes.platillos.platillos import applatillo
from routes.refrescos.refrescos import apprefresco



app = Flask(__name__)
app.register_blueprint(appalumno)
app.register_blueprint(appdisco)
app.register_blueprint(applaptop)
app.register_blueprint(applatillo)
app.register_blueprint(apprefresco)
app.register_blueprint(apperror)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")