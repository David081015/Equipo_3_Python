from flask import Flask
from database import db
from encriptador import bcrypt
from flask_migrate import Migrate
from config import BasicConfig
from flask_cors import CORS
from routes.users.users import appuser
from routes.breads.breads import appbread
from routes.pdf.pdf import apppdf

app = Flask(__name__)
app.register_blueprint(appuser)
app.register_blueprint(appbread)
app.register_blueprint(apppdf)
app.config.from_object(BasicConfig)
CORS(app)
bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)