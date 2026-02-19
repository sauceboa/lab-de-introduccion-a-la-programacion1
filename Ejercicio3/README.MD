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

## 🚀 Ejecución Directa

Si tienes Python instalado, puedes probar el script siguiendo estos pasos:

1. Descarga el archivo `AccesoUsuario.py`.
2. Abre una terminal en la carpeta del archivo.
3. Ejecuta el comando:
   ```bash
   python AccesoUsuario.py
