from flask import Flask
from flask_migrate import Migrate
from database import db
import logging
from config import BasicConfig

from routes.videojuegos.videojuegos import appvideojuego
from routes.equiposfut.equiposfuthttp import appequipofuthttp
from routes.peliculas.peliculas import apphttp,appelicula

app = Flask(__name__)
app.register_blueprint(appvideojuego)
app.register_blueprint(appequipofuthttp)
app.register_blueprint(apphttp)
app.register_blueprint(appelicula)
app.config.from_object(BasicConfig)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
logging.basicConfig(level=logging.DEBUG,filename="debug.log")