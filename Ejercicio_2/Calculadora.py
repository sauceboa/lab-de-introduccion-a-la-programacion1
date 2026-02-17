class ConversorNumerico:
    def __init__(self, numero_decimal):
        # Validamos que sea un entero
        if not isinstance(numero_decimal, int):
            raise ValueError("El valor debe ser un número entero.")
        self.numero = numero_decimal

    def _convertir_a_base(self, base):
        """Método privado reutilizable para bases 2, 8 y 16."""
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
        # En Python, cualquier número distinto de 0 es True
        return self.numero != 0

# --- Ejemplo de Uso ---
numero = 25
mi_conversor = ConversorNumerico(numero)

print(f"Decimal: {numero}")
print(f"Binario: {mi_conversor.a_binario()}")
print(f"Octal: {mi_conversor.a_octal()}")
print(f"Hexadecimal: {mi_conversor.a_hexadecimal()}")
print(f"Booleano: {mi_conversor.a_booleano()}")