from logger_base import log 

class Materia:
    def __init__(self,idmateria=None, nombre = None, creditos = None) -> None:
        self._idmateria = idmateria
        self._nombre = nombre
        self._creditos = creditos
    
    def __str__(self) -> str:
        return f"""
        ID materia: {self._idmateria}
        Nombre: {self._nombre}
        Creditos: {self._creditos}
        """
    
    @property
    def IdMateria(self):
        return self._idmateria
    @IdMateria.setter
    def idmateria(self,idmateria):
        self._idmateria = idmateria

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def Creditos(self):
        return self._creditos
    @Creditos.setter
    def creditos(self,creditos):
        self._creditos = creditos

if __name__== "__main__":
    pass