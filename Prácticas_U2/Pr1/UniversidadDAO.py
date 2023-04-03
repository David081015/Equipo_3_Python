from Universidad import Universidad 
from cursorDelPool import CursorDelPool
from logger_base import log

class UniversidadDAO:
    _SELECCIONAR = "SELECT * FROM universidad ORDER BY iduniversidad"
    _INSERTAR = "INSERT INTO universidad (nombre,direccion) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE universidad SET nombre=%s,direccion=%s WHERE iduniversidad=%s"
    _ELIMINAR = "DELETE FROM universidad WHERE iduniversidad=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            Universidades = []
            for r in registros:
                universidad = Universidad(r[0],r[1],r[2])
                Universidades.append(universidad)
            return Universidades
    @classmethod
    def insertar(cls,universidad):
        with CursorDelPool() as cursor:
            valores = (universidad.Nombre, universidad.Direccion)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,universidad):
        with CursorDelPool() as cursor:
            valores = (universidad.Nombre, universidad.Direccion, universidad.IdUniversidad)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,universidad):
        with CursorDelPool() as cursor:
            valores = (universidad.IdUniversidad,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    universidad = Universidad(nombre="UAT",direccion="Lejos")
    universidadesInsertadas = UniversidadDAO.insertar(universidad)
    log.debug(f"Universidades Agregadas {universidadesInsertadas}")

    #actualizar
    universidad = Universidad(nombre="UT",direccion="Rancho", iduniversidad="2")
    universidadesActualizadas = UniversidadDAO.actualizar(universidad)
    log.debug(f"universidades Actualizadas {universidadesActualizadas}")

    #eliminar
    universidad = Universidad(iduniversidad=3)
    universidadesEliminadas = UniversidadDAO.eliminar(universidad)
    log.debug(f"universidades Eliminadas {universidadesEliminadas}")

    #Leer
    universidades = UniversidadDAO.seleccionar()
    for u in universidades:
        log.debug(u)