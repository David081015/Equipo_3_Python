from flask import Blueprint,request,jsonify,render_template
from models import Imagen
from auth import tokenCheck
from sqlalchemy import exc
from app import db
import base64

imageUser = Blueprint('imageUser',__name__,template_folder="templates")

def render_image(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@imageUser.route("/displayImage",methods=["GET"])
@tokenCheck
def showImage(usuario):
    searchImage=Imagen.query.filter_by(user_id=usuario['user_id']).first()
    if searchImage:
        image=searchImage.rendered_data
        return render_template('PerfilDeUsuario.html',img=image)
    else:
        return jsonify({"message":"Imagen no encontrada"})
    
@imageUser.route("/uploadPerfil",methods=["POST"])
@tokenCheck
def upload(usuario):
    searchImage = Imagen.query.filter_by(user_id=usuario["user_id"]).first()
    try:
        if searchImage:
            file=request.files["inputFile"]
            data = file.read()
            render_file = render_image(data)
            searchImage.rendered_data = render_file
            searchImage.data = data
            db.session.commit()
            return jsonify({"message":"imagen actualizada"})
        else:
            file=request.files["inputFile"]
            data = file.read()
            render_file = render_image(data)
            newFile = Imagen()
            newFile.type="Perfil"
            newFile.rendered_data = render_file
            newFile.user_id = usuario['user_id']
            newFile.data = data
            db.session.add(newFile)
            db.session.commit()
            return jsonify({"message":"imagen agregada"})
    except exc.SQLAlchemyError as e:
        return jsonify({"message":e})