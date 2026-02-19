intentos = 3

while intentos > 0:
    print(f"INICIO DE SESIÓN (INTENTOS RESTANTES: {intentos})")
    
    UsuarioNombre = input("Usuario: ")
    UsuarioContraseña = input("Contraseña: ")
    tiene_numero = any(c.isdigit() for c in UsuarioContraseña)
    tiene_letra = any(c.isalpha() for c in UsuarioContraseña)
    masde8 = len(UsuarioContraseña) >= 8
    error_detectado = False

    if not UsuarioNombre.isalnum():
        print("Error: El usuario no puede estar vacío ni tener símbolos ni espacios.")
        error_detectado = True
    elif UsuarioNombre != "Admin":
        print("Error: Usuario incorrecto.")
        error_detectado = True
    if masde8 == False:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        error_detectado = True
    if tiene_letra == False or tiene_numero == False:
        print("Error: La contraseña debe tener al menos una letra y un número.")
        error_detectado = True
    if error_detectado == False and UsuarioContraseña != "Admin2026":
        print("Error: La contraseña es incorrecta.")
        error_detectado = True
    if error_detectado == False:
        print(f"¡BIENVENIDO {UsuarioNombre}! ACCESO EXITOSO")
        break
    else:
        intentos -= 1
if intentos == 0:
    print("Acceso bloqueado. Has agotado tus 3 intentos.")

