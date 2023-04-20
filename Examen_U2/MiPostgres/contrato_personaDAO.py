from contrato_persona import contrato_persona 
from cursorDelPool import CursorDelPool
from logger_base import log

class contrato_personaDAO:
    _SELECCIONAR = "SELECT * FROM contrato_persona ORDER BY idcontratopersona"
    _INSERTAR = "INSERT INTO persona (idcontrato,idpersona) VALUES (%s,%s)"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratas = []
            for r in registros:
                cp = contrataspersonas(r[0],r[1],r[2])
                contratas.append(cp)
            return contratas
    @classmethod
    def insertar(cls,contrato_persona):
        with CursorDelPool() as cursor:
            valores = (contrato_persona.idpersona, contrato_persona.idcontrato)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount

        
if __name__ == "__main__":
    #insertar
    #persona1 = Persona(nombre="Pedro",apellido="Pascal",email="ppascal@gmail.com",edad=35)
    cp1 = contrato_persona(1,1)
    #personasInsertadas = PersonaDAO.insertar(persona1)
    cpInsertardos = contrato_personaDAO.insertar(cp1)
    log.debug(f"ContratoPersona Agregadas {cpInsertardos}")
    #Leer
    contrataspersonas = contrato_personaDAO.seleccionar()
    for p in contrataspersonas:
        log.debug(p)