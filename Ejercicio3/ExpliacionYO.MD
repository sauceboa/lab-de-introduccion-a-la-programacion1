# Sistema de Autenticación en Python

Pues lo que realizamos en clase fue un inicio de sesion con restricciones utilizando como lenguage de programacion python basicamente al inicio tienes una variable de intentos (maximos 3 intentos)

se inicio poniendo las variables:
---

**intentos**: basicamente es la variable que limita los intentos y controla el bucle`while`.
* **UsuarioNombre**: esta variable guarda el usuario 
* **UsuarioContraseña**: guarda la contraseña
* **tiene_numero**: variable que verifica que haya digitos`any(c.isdigit())`.
* **tiene_letra**: variable que verifica que haya caracteres alfabéticos `any(c.isalpha())`.
* **masde8**: Variable que comprueba si la longitud de la cadena es `>= 8`.
* **error_detectado**: es la variable que comprueba la presencia de algun tipo de error y si se resta un intento o permite el acceso 

y ahora dejando afuera las variables vamos a hablar acerca de el funcionamiento del Codigo resumidamente 

1. **Entrada de datos**: El codigo solicita las credenciales al inicio de cada ciclo del bucle `while`.
2. **Evaluación de requisitos**: Se guardan las variables `tiene_numero`, `tiene_letra` y `masde8` basándose en la contraseña ingresada.
3. **Validación de Usuario**:
   - verifica que es alfanumerico `.isalnum()`.
   - compara que el valor sea  `Admin`.
4. **Validación de Contraseña**:
   - verifica que cumpla con el mínimo de 8 caracteres
   - verifica que contenga la combinación de letras y números
5. **Control de flujo**:
   - Si `error_detectado` es `True`, se resta 1 a `intentos`.
   - Si `error_detectado` es `False`, se imprime el mensaje de éxito y se ejecuta `break`.
