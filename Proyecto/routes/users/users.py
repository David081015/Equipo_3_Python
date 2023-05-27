from flask import Blueprint,request,jsonify,render_template
from sqlalchemy import exc 
from models import Usuario
from app import db,bcrypt
from auth import tokenCheck,verificarToken

appuser=Blueprint('appuser',__name__,template_folder='templates')

@appuser.route('/usuarios',methods=["GET"])
@tokenCheck
def getUsers(usuario):
    print(usuario)
    if(usuario['admin']):
        response=[]
        usuarios = Usuario.query.all()
        for usuario in usuarios:
            usuarioData={
                'id':usuario.id,
                'nombre':usuario.nombre,
                'email':usuario.email,
                'password':usuario.password,
                'registrado':usuario.registrado,
                'admin':usuario.admin
            }
            response.append(usuarioData)
        return jsonify({'usuarios':response})  
    else: 
        return jsonify({"message":"Acceso denegado"}) 

@appuser.route('/')
@appuser.route('/index')
def index():
    return render_template('index.html')

@appuser.route('/main')
def main():
    nombre_usuario = request.args.get('nombre_usuario')
    return render_template('main.html', nombre_usuario=nombre_usuario)

@appuser.route('/mainAdmin')
def mainAdmin():
    return render_template('mainAdmin.html')

@appuser.route('/error')
def error():
    return render_template('error.html')

@appuser.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error.html', error=error),404

@appuser.route('/perfil')
def perfil():
    nombre_usuario = request.args.get('nombre_usuario') # Obtener el nombre de usuario de la URL
    return render_template('perfil.html', nombre_usuario=nombre_usuario)

@appuser.route('/login',methods=["GET","POST"])
def login_post():
    if(request.method=="GET"):
        token = request.args.get('token')
        if token:
            info = verificarToken(token)
            if(info['status']!='fail'):
                responseObject={
                    'status':'success',
                    'message':'valid token',
                    'info':info
                }
                return jsonify(responseObject)
        return render_template('login.html')
    else:
        email = request.json['email']
        password=request.json['password']
        consulta= Usuario.query.filter_by(email=email).first()
        nombre = consulta.nombre
        usuario = Usuario(nombre=nombre,email=email,password=password)
        userFilter=Usuario.query.filter_by(email=usuario.email).first()
        if userFilter:
            validation=bcrypt.check_password_hash(userFilter.password,password)
            if validation:
                auth_token = usuario.encode_auth_token(userFilter.id)
                response= {
                    'status':'success',
                    'message':'Loggin exitoso',
                    'auth_token':auth_token,
                    'user_bool': userFilter.admin,
                    'nombre_usuario': userFilter.nombre
                }
                return jsonify(response)
        return jsonify({"message":"Datos incorrectos"})

@appuser.route('/signin',methods=["GET","POST"])
def registrar():
    if request.method=="GET":
        return render_template('registrar.html')
    else:
        nombre = request.json["nombre"]
        email = request.json["email"]
        password=request.json["password"]
        usuario = Usuario(nombre=nombre,email=email,password=password)
        userExists=Usuario.query.filter_by(email=email).first()
        if not userExists:
            try:   
                db.session.add(usuario)
                db.session.commit()
                responseObject={
                    "status":"success",
                    "message":"Registro Exitoso"
                }
            except Exception as e:
                responseObject={
                    "status":"Error",
                    "message": e
                }
        else:
            responseObject={
                "status":"Error",
                "message":"Ya existe el usuario"
            }
        return jsonify(responseObject)