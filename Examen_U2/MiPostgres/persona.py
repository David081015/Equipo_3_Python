from logger_base import log 

class Persona:
    def __init__(self,idPersona=None, nombre = None, edad = None,email = None) -> None:
        self._idPersona = idPersona
        self._nombre = nombre
        self._email = email
        self._edad = edad
    
    def __str__(self) -> str:
        return f"""
        ID PERSONA: {self._idPersona}
        Nombre: {self._nombre}
        Email: {self._email}
        Edad: {self._edad}
        """
    
    @property
    def idPersona(self):
        return self._idPersona
    @idPersona.setter
    def idPersona(self,idPersona):
        self._idPersona = idPersona

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def Email(self):
        return self._email
    @Email.setter
    def email(self,email):
        self._email = email

    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def edad(self,edad):
        self._edad = edad

if __name__== "__main__":
    persona1 = Persona(1,"Juan",28,"Jperez@gmail.com")
    log.debug(persona1)