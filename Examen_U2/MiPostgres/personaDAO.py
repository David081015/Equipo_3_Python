from persona import Persona 
from cursorDelPool import CursorDelPool
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY idpersona"
    _INSERTAR = "INSERT INTO persona (nombre,edad,email) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s,edad=%s, email=%s WHERE idpersona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE idpersona=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad,persona.Email)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.Nombre, persona.Edad,persona.Email, persona.idPersona)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.idPersona,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    #persona1 = Persona(nombre="Pedro",apellido="Pascal",email="ppascal@gmail.com",edad=35)
    persona2 = Persona(nombre="David",edad=22,email="macpollo@gmail.com")
    #personasInsertadas = PersonaDAO.insertar(persona1)
    personasInsertadas = PersonaDAO.insertar(persona2)
    log.debug(f"Personas Agregadas {personasInsertadas}")
    #Leer
    personas = PersonaDAO.seleccionar()
    for p in personas:
        log.debug(p)