from flask import Blueprint,make_response,render_template
from models import Usuario
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

appbread= Blueprint('appbread',__name__,template_folder="templates")