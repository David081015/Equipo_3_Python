from Alumno import Alumno 
from cursorDelPool import CursorDelPool
from logger_base import log

class AlumnoDAO:
    _SELECCIONAR = "SELECT * FROM alumno ORDER BY num_control"
    _INSERTAR = "INSERT INTO alumno (nombre,apellido,edad) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE alumno SET nombre=%s,apellido=%s,edad=%s WHERE num_control=%s"
    _ELIMINAR = "DELETE FROM alumno WHERE num_control=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            alumnos = []
            for r in registros:
                alumno = Alumno(r[0],r[1],r[2],r[3])
                alumnos.append(alumno)
            return alumnos
    @classmethod
    def insertar(cls,alumno):
        with CursorDelPool() as cursor:
            valores = (alumno.Nombre, alumno.Apellido, alumno.Edad)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,alumno):
        with CursorDelPool() as cursor:
            valores = (alumno.Nombre, alumno.Apellido, alumno.Edad, alumno.Num_Control)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,alumno):
        with CursorDelPool() as cursor:
            valores = (alumno.Num_Control,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    alumno = Alumno(nombre="Pedro",apellido="Pascal",edad=45)
    alumnosInsertados = AlumnoDAO.insertar(alumno)
    log.debug(f"Alumnos Agregados {alumnosInsertados}")
    #Leer
    alumnos = AlumnoDAO.seleccionar()
    for a in alumnos:
        log.debug(a)