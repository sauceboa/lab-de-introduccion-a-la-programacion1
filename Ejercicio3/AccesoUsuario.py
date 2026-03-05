intentos = 3
acceso_concedido = False 

while intentos > 0:
    print(f"\nINICIO DE SESIÓN (INTENTOS RESTANTES: {intentos})")
    
    UsuarioNombre = input("Usuario: ")
    UsuarioContraseña = input("Contraseña: ")
    
    # Validaciones de contraseña
    tiene_numero = any(c.isdigit() for c in UsuarioContraseña)
    tiene_letra = any(c.isalpha() for c in UsuarioContraseña)
    masde8 = len(UsuarioContraseña) >= 8
    error_detectado = False

    # Lógica de validación
    if not UsuarioNombre.isalnum():
        print("Error: El usuario no puede estar vacío ni tener símbolos.")
        error_detectado = True
    elif UsuarioNombre != "Admin":
        print("Error: Usuario incorrecto.")
        error_detectado = True
    elif not masde8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        error_detectado = True
    elif not tiene_letra or not tiene_numero:
        print("Error: La contraseña debe tener letra y número.")
        error_detectado = True
    elif UsuarioContraseña != "Admin2026":
        print("Error: Contraseña incorrecta.")
        error_detectado = True
    
    if not error_detectado:
        print(f"¡BIENVENIDO {UsuarioNombre}! ACCESO EXITOSO")
        acceso_concedido = True
        
        # MENÚ
        while acceso_concedido:
            print("\n1. Clasificar Número\n2. Categoría edad\n3. Calcular tarifa\n4. Cerrar sesión\n5. Salir")
            seleccion = input("Opción: ")
            
            if seleccion == "1":
                print("--- Ejecutando: Número clasificado ---")
                while True:
                    try:
                        num = int(input("Ingrese un número: "))
                        if num > 0:
                            print(f"El número {num} es positivo.")
                        elif num < 0:
                            print(f"El número {num} es negativo.")
                        else:
                            print(f"El número {num} es cero.")
                        if num % 2 == 0:
                            print(f"El número {num} es par.")
                        if num % 2 != 0:
                            print(f"El número {num} es impar.")
                        break
                    except ValueError:
                        print("Error: Debe ingresar un número entero válido.")
            elif seleccion == "2":
                print("--- Ejecutando: Categoría de edad ---")
                while True:
                        try:
                            edad = int(input("Ingrese la edad: "))
                            if edad < 0:
                                print("Error: La edad no puede ser negativa.")
                            elif edad <= 12:
                                print(f"Con {edad} años, eres un niño.")
                            elif edad <= 17:
                                print(f"Con {edad} años, eres un adolescente.")     
                            elif edad <= 64:
                                print(f"Con {edad} años, eres un adulto.")
                                print("Cuentas con identificacion oficial S/N?")
                                identificacion = input("Respuesta (S/N): ").strip().upper()
                                if identificacion == "S":
                                    print("Puedes conducir un vehículo.")
                                    print("Cuentas Con licencia de conducir S/N?")
                                if identificacion == "N":
                                    print("No puedes conducir un vehículo.")
                                    licencia = input("Respuesta (S/N): ").strip().upper()
                                    if licencia == "S":
                                        print("Puedes conducir un vehículo.")
                            else:
                                print(f"Con {edad} años, eres un adulto mayor.")
                            break
                        except ValueError:
                            print("Error: Debe ingresar una edad válida (número entero).")  
            elif seleccion == "3":
                print("--- Ejecutando: Calcular Tarifa ---")
            elif seleccion == "4":
                print("Cerrando Sesión...")
                acceso_concedido = False # Rompe el bucle del menú
                intentos = 3 
            elif seleccion == "5":
                print("Saliendo del programa.")
                exit()
            else:
                print("Opción no válida.")
        
     
    

if intentos == 0 and not acceso_concedido:
    print("\nAcceso bloqueado. Has agotado tus 3 intentos.") 

