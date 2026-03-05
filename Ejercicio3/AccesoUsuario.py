import sys

def clasificar_numero():
    print("\n--- Ejecutando: Número clasificado ---")
    try:
        num = int(input("Ingrese un número: "))
        # Clasificación por signo
        match num:
            case n if n > 0: print(f"El número {n} es positivo.")
            case n if n < 0: print(f"El número {n} es negativo.")
            case _: print("El número es cero.")
        
        # Clasificación par/impar
        match num % 2:
            case 0: print(f"El número {num} es par.")
            case _: print(f"El número {num} es impar.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

def categoria_edad():
    print("\n--- Ejecutando: Categoría de edad ---")
    try:
        edad = int(input("Ingrese la edad: "))
        match edad:
            case e if e < 0: print("Error: La edad no puede ser negativa.")
            case e if e <= 12: print(f"Con {e} años, eres un niño.")
            case e if e <= 17: print(f"Con {e} años, eres un adolescente.")
            case e if e <= 64:
                print(f"Con {e} años, eres un adulto.")
                id_oficial = input("¿Cuentas con identificación oficial? (S/N): ").upper()
                match id_oficial:
                    case "S": print("Puedes conducir un vehículo.")
                    case "N": print("No puedes conducir sin identificación.")
                    case _: print("Opción no válida.")
            case _: print(f"Con {edad} años, eres un adulto mayor.")
    except ValueError:
        print("Error: Ingrese un número entero.")

def calcular_tarifa():
    print("\n--- Ejecutando: Calcular Tarifa Final ---")
    try:
        precio_base = 100
        dia = int(input("Ingrese día de la semana (1-7): "))
        match dia:
            case d if 1 <= d <= 7:
                total = precio_base
                if d in [6, 7]:
                    total += 20
                    print("+ Recargo de fin de semana ($20).")
                if input("¿Eres estudiante? (S/N): ").upper() == "S":
                    total *= 0.85
                    print("- Descuento estudiante (15%).")
                if input("¿Eres miembro? (S/N): ").upper() == "S":
                    total *= 0.9
                    print("- Descuento miembro (10%).")
                print(f"Tarifa final: ${total:.2f}")
            case _:
                print("Día inválido.")
    except ValueError:
        print("Error: Datos inválidos.")

def validar_acceso(usuario, password):
    # Criterios lógicos
    es_alfanumerico = usuario.isalnum()
    es_admin = usuario == "Admin"
    masde8 = len(password) >= 8
    tiene_numero = any(c.isdigit() for c in password)
    tiene_letra = any(c.isalpha() for c in password)
    clave_correcta = password == "Admin2026"

    # Match case para capturar errores específicos
    match (es_alfanumerico, es_admin, masde8, tiene_numero, tiene_letra, clave_correcta):
        case (False, _, _, _, _, _):
            print("Error: El usuario no puede estar vacío ni tener símbolos.")
            return False
        case (_, False, _, _, _, _):
            print("Error: Usuario incorrecto.")
            return False
        case (_, _, False, _, _, _):
            print("Error: La contraseña debe tener al menos 8 caracteres.")
            return False
        case (_, _, _, False, _, _) | (_, _, _, _, False, _):
            print("Error: La contraseña debe tener letra y número.")
            return False
        case (_, _, _, _, _, False):
            print("Error: Contraseña incorrecta.")
            return False
        case (True, True, True, True, True, True):
            return True


intentos = 3

while intentos > 0:
    # --- PARTE 1: INICIO DE SESIÓN ---
    print(f"\n{'='*30}\nINICIO DE SESIÓN\n(Intentos restantes: {intentos})\n{'='*30}")
    user_input = input("Usuario: ")
    pass_input = input("Contraseña: ")

    if validar_acceso(user_input, pass_input):
        print(f"\n¡ACCESO EXITOSO! BIENVENIDO, {user_input.upper()}.")
        
        # --- PARTE 2: MENÚ (Solo si el login fue exitoso) ---
        while True:
            print("\n" + "--- MENÚ PRINCIPAL ---")
            print("1. Clasificar Número")
            print("2. Categoría edad")
            print("3. Calcular tarifa")
            print("4. Cerrar sesión")
            print("5. Salir")
            
            seleccion = input("Seleccione una opción: ")
            
            match seleccion:
                case "1": clasificar_numero()
                case "2": categoria_edad()
                case "3": calcular_tarifa()
                case "4":
                    print("\nCerrando Sesión... Volviendo al Login.")
                    intentos = 3 # Reiniciamos intentos para el próximo usuario
                    break        # Sale del menú, vuelve al ciclo de login
                case "5":
                    print("Saliendo del programa. ¡Adiós!")
                    sys.exit()
                case _:
                    print("Opción no válida. Intente de nuevo.")
    else:
        intentos -= 1

# Si sale del bucle while porque intentos llegó a 0
if intentos == 0:
    print("ACCESO BLOQUEADO. Agotó sus 3 intentos.")
