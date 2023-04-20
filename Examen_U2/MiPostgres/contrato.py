from logger_base import log 

class Contrato:
    def __init__(self,idContrato=None, noContrato = None, fechaInicio = None, fechaFin = None) -> None:
        self._idContrato = idContrato
        self._noContrato = noContrato
        self._fechaInicio = fechaInicio
        self._fechaFin = fechaFin
    
    def __str__(self) -> str:
        return f"""
        ID Contrato: {self._idContrato}
        noContrato: {self._noContrato}
        fechaInicio: {self._fechaInicio}
        fechaFin: {self._fechaFin}
        """
    

if __name__== "__main__":
    contrato1 = Contrato(1,1,'10/1/2001','10/1/2001')
    log.debug(contrato1)