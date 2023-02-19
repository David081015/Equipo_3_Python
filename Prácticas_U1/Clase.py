class Usuario:
    def __init__(self, Usuario, Contraseña, Rol, Nombre, Curp, Ciudad) -> None:
        self._Usuario = Usuario
        self._Contraseña = Contraseña
        self._Rol = Rol
        self._Nombre = Nombre
        self._Curp = Curp
        self._Ciudad = Ciudad
    @property
    def UsuarioP(self):
        return self._Usuario
    @property
    def Contraseña(self):
        return self._Contraseña
    @property
    def Rol(self):
        return self._Rol
    @property
    def Nombre(self):
        return self._Nombre
    @property
    def Curp(self):
        return self._Curp
    @property
    def Ciudad(self):
        return self._Ciudad