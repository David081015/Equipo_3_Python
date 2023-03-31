from logger_base import log 

class Universidad:
    def __init__(self,iduniversidad=None, nombre = None, direccion = None) -> None:
        self._iduniversidad = iduniversidad
        self._nombre = nombre
        self._direccion = direccion
    
    def __str__(self) -> str:
        return f"""
        ID universidad: {self._iduniversidad}
        Nombre: {self._nombre}
        Direccion: {self._direccion}
        """
    
    @property
    def IdUniversidad(self):
        return self._iduniversidad
    @IdUniversidad.setter
    def IdUniversidad(self,idu_iduniversidad):
        self._iduniversidad = idu_iduniversidad

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def Direccion(self):
        return self._direccion
    @Direccion.setter
    def Direccion(self,direccion):
        self._direccion = direccion

if __name__== "__main__":
    pass