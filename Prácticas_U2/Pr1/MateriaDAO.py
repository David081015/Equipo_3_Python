from Materia import Materia
from cursorDelPool import CursorDelPool
from logger_base import log

class MateriaDAO:
    _SELECCIONAR = "SELECT * FROM materia ORDER BY idmateria"
    _INSERTAR = "INSERT INTO materia (nombre,creditos) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE materia SET nombre=%s,creditos=%s WHERE idmateria=%s"
    _ELIMINAR = "DELETE FROM materia WHERE idmateria=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            materias = []
            for r in registros:
                materia = Materia(r[0],r[1],r[2])
                materias.append(materia)
            return materias
    @classmethod
    def insertar(cls,materia):
        with CursorDelPool() as cursor:
            valores = (materia.Nombre, materia.Creditos)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,materia):
        with CursorDelPool() as cursor:
            valores = (materia.Nombre, materia.Creditos, materia.IdMateria)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,materia):
        with CursorDelPool() as cursor:
            valores = (materia.IdMateria,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    # materia = Materia(nombre="C",creditos=11)
    # materiasInsertadas = MateriaDAO.insertar(materia)
    # log.debug(f"Materias Agregadas {materiasInsertadas}")

    #actualizar
    # materia = Materia(nombre="C#",creditos=6,idmateria="2")
    # materiasActualizadas = MateriaDAO.actualizar(materia)
    # log.debug(f"Materias Actualizadas {materiasActualizadas}")

    #eliminar
    # materia = Materia(idmateria=3)
    # materiasEliminadas = MateriaDAO.eliminar(materia)
    # log.debug(f"Materias Eliminadas {materiasEliminadas}")

    #Leer
    materias = MateriaDAO.seleccionar()
    for m in materias:
        log.debug(m)