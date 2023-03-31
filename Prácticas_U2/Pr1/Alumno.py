from logger_base import log 

class Alumno:
    def __init__(self,num_control=None, nombre = None, apellido = None, edad = None) -> None:
        self._num_control = num_control
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    
    def __str__(self) -> str:
        return f"""
        N°Control: {self._num_control}
        Nombre: {self._nombre}
        Apellido: {self._apellido}
        Edad: {self._edad}
        """
    
    @property
    def Num_Control(self):
        return self._num_control
    @Num_Control.setter
    def Num_Control(self,num_control):
        self._num_control = num_control

    @property
    def Nombre(self):
        return self._nombre
    @Nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def Apellido(self):
        return self._apellido
    @Apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido
    
    @property
    def Edad(self):
        return self._edad
    @Edad.setter
    def edad(self,edad):
        self._edad = edad

if __name__== "__main__":
    alumno1 = Alumno(1,"Juan","Perez",28)
    log.debug(alumno1)
