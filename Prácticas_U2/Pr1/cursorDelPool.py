from logger_base import log
from Conexion import Conexion

class CursorDelPool:
    def __init__(self) -> None:
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug("Entra with")
        self._conexion = Conexion.ObtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self,tipoExcepcion,mensajeExcepcion,detalleExcepcion):
        log.debug("Sale with")
        if mensajeExcepcion:
            log.debug("Error", mensajeExcepcion)
            self._conexion.rollback()
        else:
            self._conexion.commit()
        self._cursor.close()
        Conexion.LiberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())