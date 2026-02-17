# Ejercicio 2: Conversor Numérico (Clase Python)

Este proyecto consiste en el desarrollo de una clase en Python que permite convertir números decimales a diferentes sistemas de numeración (Binario, Octal, Hexadecimal) y su representación booleana. 

## 🚀 Funcionalidades

La clase `ConversorNumerico` incluye métodos para convertir un número entero positivo a:
* **Binario (Base 2)**
* **Octal (Base 8)**
* **Hexadecimal (Base 16)**
* **Booleano** (Identifica si el número es `True` o `False`)

## 🛠️ Explicación del Código

### 1. Estructura de la Clase
Se utiliza el método constructor `__init__` para recibir el número decimal y validar que sea un número entero.

### 2. Reutilización de Código 
En lugar de repetir la lógica de conversión, se creó un método maestro llamado `_convertir_a_base(self, base)`. Este método utiliza:
* **Operador Módulo (`%`)**: Para obtener el residuo que corresponde al dígito en la nueva base.
* **División de Piso (`//`)**: Para actualizar el número decimal y continuar las divisiones sucesivas.
* **Bucle `while`**: Para iterar hasta que el cociente sea cero.

### 3. Representación Booleana
Se aplica la lógica de programación donde el número `0` equivale a `False` y cualquier otro valor equivale a `True`.

### 4. Pasos para guardar desde Terminal a github 

`git add .
git commit -m "Entrega Ejercicio 2: Conversor de bases"
git push origin main`.

## 💻 Código de la Calculadora

```python
class ConversorNumerico:
    def __init__(self, numero_decimal):
        if not isinstance(numero_decimal, int):
            raise ValueError("El valor debe ser un número entero.")
        self.numero = numero_decimal

    def _convertir_a_base(self, base):
        if self.numero == 0:
            return "0"
        
        digitos = "0123456789ABCDEF"
        resultado = ""
        temp_num = self.numero

        while temp_num > 0:
            residuo = temp_num % base
            resultado = digitos[residuo] + resultado
            temp_num = temp_num // base
        
        return resultado

    def a_binario(self):
        return self._convertir_a_base(2)

    def a_octal(self):
        return self._convertir_a_base(8)

    def a_hexadecimal(self):
        return self._convertir_a_base(16)

    def a_booleano(self):
        return self.numero != 0

# Ejemplo de ejecución
numero = 25
mi_conversor = ConversorNumerico(numero)

print(f"Decimal: {numero}")
print(f"Binario: {mi_conversor.a_binario()}")
print(f"Octal: {mi_conversor.a_octal()}")
print(f"Hexadecimal: {mi_conversor.a_hexadecimal()}")
print(f"Booleano: {mi_conversor.a_booleano()}")


