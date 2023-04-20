from contrato import Contrato 
from cursorDelPool import CursorDelPool
from logger_base import log

class ContratoDAO:
    _SELECCIONAR = "SELECT * FROM contrato ORDER BY idContrato"
    _INSERTAR = "INSERT INTO contrato (noContrato,costo,fechaInicio,fechaFin) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET noContrato=%s,costo=%s, fechaInicio=%s, fechaFin=%s WHERE idContrato=%s"
    _ELIMINAR = "DELETE FROM contrato WHERE idContrato=%s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(Contrato)
            return contratos
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.noContrato, contrato.Costo,contrato.fechaInicio,contrato.fechaFin)
            cursor.execute(cls._INSERTAR,valores)
            return cursor.rowcount
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.noContrato, contrato.Costo,contrato.fechaInicio,contrato.fechaFin,contrato.idContrato)
            cursor.execute(cls._ACTUALIZAR,valores)
            return cursor.rowcount
    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.idContrato,)
            cursor.execute(cls._ELIMINAR,valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #insertar
    #persona1 = Contrato(nombre="Pedro",apellido="Pascal",email="ppascal@gmail.com",edad=35)
    contrato1 = Contrato(noContrato=1,Costo=22,fechaInicio='13/12/2001',fechaFin='13/12/2001')
    #personasInsertadas = PersonaDAO.insertar(persona1)
    contratosInsertados = ContratoDAO.insertar(contrato1)
    log.debug(f"Personas Agregadas {contratosInsertados}")
    #Leer
    contratos = ContratoDAO.seleccionar()
    for p in contratos:
        log.debug(p)