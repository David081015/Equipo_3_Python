from flask import Blueprint,render_template

apperror= Blueprint('apperror',__name__,template_folder="templates")

@apperror.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('error404.html', error=error),404