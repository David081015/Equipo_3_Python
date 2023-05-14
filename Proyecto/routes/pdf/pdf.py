from flask import Blueprint,make_response,render_template
from models import Usuario
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

apppdf = Blueprint('apppdf',__name__,template_folder="templates")

@apppdf.route('/generatePdf')
def generatePdf():
    usuarios=Usuario.query.all()
    listaUsuarios=[["ID","EMAIL","REGISTRADO","ADMIN"]]
    for usuario in usuarios:
        listaUsuarios.append([
            usuario.id,
            usuario.email,
            usuario.registrado,
            usuario.admin
        ])
    doc = SimpleDocTemplate("users.pdf",pagesize=letter)
    table=Table(listaUsuarios)

    tableStyle = TableStyle([
        ('BACKGROUND',(0,0),(-1,0),colors.grey),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
        ('FONTSIZE',(0,0),(-1,0),16),
        ('BOTTOMPADDING',(0,0),(-1,0),12),
        ('BACKGROUND',(0,1),(-1,-1),colors.white),
        ('GRID',(0,0),(-1,-1),1,colors.black)
        ])
    table.setStyle(tableStyle)

    text="LISTADO DE USUARIOS"
    textStyle = getSampleStyleSheet()["Normal"]
    textStyle.alignment=TA_CENTER
    paragraph=Paragraph(text,textStyle)
    elementos=[paragraph,table]
    doc.build(elementos)

    response =make_response(open("users.pdf","rb").read())
    response.headers['Content-Type']="application/pdf"
    response.headers['Content-Disposition']='inline;filename=users.pdf'
    return response

@apppdf.route('/Pdf')
def index():
    return render_template('indexPdf.html')