# Sistema de Autenticación en Python 🔐

Este proyecto consiste en un script de Python que simula un inicio de sesión seguro con validaciones detalladas de usuario y contraseña, limitando el acceso a un máximo de 3 intentos fallidos.

---

## 📋 Requisitos de Acceso

Para ingresar al sistema, las credenciales deben ser:
* **Usuario:** `Admin`
* **Contraseña:** `Admin2026`

---

## 🛠️ Funcionalidades y Validaciones

El script utiliza un sistema de **banderas (`error_detectado`)** para evaluar múltiples condiciones antes de decidir si descuenta un intento o concede el acceso.

### 1. Gestión de Intentos
* Se inicia con un contador de **3 intentos**.
* El bucle `while intentos > 0` mantiene el programa activo hasta que se agotan las oportunidades o el ingreso es exitoso.

### 2. Filtros de Usuario
* **Validación de Caracteres:** Mediante `.isalnum()`, se asegura que el usuario no contenga espacios ni símbolos especiales.
* **Identidad:** Solo se permite el nombre de usuario exacto `Admin`.

### 3. Seguridad de Contraseña
La contraseña se somete a tres filtros de seguridad:
* **Longitud:** Debe tener al menos **8 caracteres** (validado con `len()`).
* **Contenido Alfanumérico:** Debe poseer letras y números simultáneamente.
* **Lógica de Verificación:** Se utilizan las funciones `any(c.isdigit()...)` y `any(c.isalpha()...)` para recorrer la cadena y confirmar la presencia de caracteres válidos.

---

## 💻 Estructura del Código

El flujo lógico implementado en `AccesoUsuario.py` es el siguiente:

1. **Entrada de Datos:** Captura del nombre y la contraseña del usuario.
2. **Evaluación Técnica:** Se definen las variables booleanas (`tiene_numero`, `tiene_letra`, `masde8`) al inicio de cada ciclo.
3. **Reporte de Errores:** Se imprimen mensajes específicos para cada fallo detectado, permitiendo al usuario saber exactamente qué debe corregir.
4. **Validación Final:** Si no se detectan errores técnicos y la contraseña coincide con el registro, se muestra el mensaje de **"ACCESO EXITOSO"**.


---


## Sistema de Acceso de Usuario 🚀

Este script de Python gestiona el inicio de sesión de un administrador mediante validaciones de seguridad y un sistema de intentos limitados.

---

## Código Fuente

```python
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
