from Clase import *
ListaUsuarios = []
UsuarioNuevo = Usuario
ListaUsuarios.append(UsuarioNuevo("Admin","123","Administrador","David","C123","Nuevo Laredo"))
Salir = False
S = False
while(Salir==False):
    print("Bienvenido \n1- Registro \n2-Inicio de sesión \n3-Salida")
    op = int(input())
    if op == 1:
        print("\nIngrese su usuario")
        usuario = input()
        print("\nIngrese su contraseña")
        contraseña = input()
        rol = "cliente"
        print("\nIngrese su nombre")
        nombre = input()
        while(S == False):
            print("\nIngrese su CURP")
            curp = input()
            for U in ListaUsuarios:
                    UsuarioNuevo = U
                    if UsuarioNuevo.Curp == curp:
                        print("\nEl usuario ya existe")
                        break
                    else:
                        UsuarioNuevo = Usuario
                        S = True
                        break
        print("\nIngrese su ciudad")
        ciudad = input()
        print("\n")
        ListaUsuarios.append(UsuarioNuevo(usuario,contraseña, rol, nombre, curp, ciudad))
        S = False
    if op == 2:
        UsuarioNuevo = Usuario
        Num = 0
        print("\nIngrese su usuario")
        usuario = input()
        print("\nIngrese su contraseña")
        contraseña = input()
        if usuario=="Admin":
            print("\nLista de usuarios: ")
            for U in ListaUsuarios:
                Num = Num + 1 
                UsuarioNuevo = U
                print(f"Número: {Num}")
                print(f"Usuario: {UsuarioNuevo.UsuarioP}, Contraseña: {UsuarioNuevo.Contraseña}, Rol: {UsuarioNuevo.Rol}, Nombre: {UsuarioNuevo.Nombre}, CURP: {UsuarioNuevo.Curp}, Ciudad: {UsuarioNuevo.Ciudad} \n")
        else:
            Entro = False
            for U in ListaUsuarios:
                UsuarioNuevo = U
                if UsuarioNuevo.UsuarioP == usuario and UsuarioNuevo.Contraseña == contraseña:
                    Entro = True
                    print(f"\nUsuario: {UsuarioNuevo.UsuarioP} \nContraseña: {UsuarioNuevo.Contraseña} \nRol: {UsuarioNuevo.Rol} \nNombre: {UsuarioNuevo.Nombre} \nCURP: {UsuarioNuevo.Curp} \nCiudad: {UsuarioNuevo.Ciudad} \n")
            if Entro==False:
                print("Datos incorrectos \n")
    if op == 3:
        Salir=True   