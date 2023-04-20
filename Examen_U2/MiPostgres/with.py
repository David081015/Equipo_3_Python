import psycopg2
from logger_base import log

conexion = psycopg2.connect(user="postgres",
                            password="Castillo105.dct",
                            host="127.0.0.1",
                            port="5432",
                            database="clase_db")
log.debug(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO cliente(nombre,apellido,email) Values(%s,%s,%s)"
            valores = (
                ("David","Castillo","DC@gmail.com"),
                ("Eduardo","Perez","EP@gmail.com")
                )
            cursor.executemany(sentencia,valores)
            registrosInsert = cursor.rowcount
            log.debug(f"Registros insertados: {registrosInsert}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE cliente SET nombre=%s, apellido=%s, email=%s WHERE idcliente = %s"
            valores = (
                ("Daniel","Tellez","DT@gmail.com",1),
                ("Polar","Escobar","PE@gmail.com",2)
            )
            cursor.executemany(sentencia, valores)
            registrosActualizados = cursor.rowcount
            log.debug(f"Registros actualizados: {registrosActualizados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM cliente WHERE idcliente=%s"
            valores = ("3")
            cursor.executemany(sentencia, valores)
            registrosEliminados = cursor.rowcount
            log.debug(f"Registros eliminados: {registrosEliminados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM cliente WHERE idcliente IN %s"
            entrada = input("IDs a eliminar")
            valores = (tuple(entrada.split(",")),)
            cursor.executemany(sentencia, valores)
            registrosEliminados = cursor.rowcount
            log.debug(f"Registros eliminados: {registrosEliminados}")
except Exception as e:
    log.error(e)
finally:
    conexion.close()