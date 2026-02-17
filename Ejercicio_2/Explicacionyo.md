
Al definir `def __init__(self, numero_decimal):`, mi objetivo fue asegurar la integridad de los datos desde el inicio. Utilicé `isinstance()` para verificar que el valor que puse sea un entero, evitando errores de ejecución si se intenta procesar un texto o un flotante.

(`_convertir_a_base`)
En lugar de escribir algoritmos separados, identifiqué que la conversión a binario (base 2), octal (base 8) y hexadecimal (base 16) sigue el mismo patrón matemático: **divisiones sucesivas**.

* **El Bucle `while`**: El programa divide el número decimal entre la base elegida hasta que el cociente llega a cero.
* **Residuos y Cocientes**: Utilicé el operador `%` para obtener el residuo (que es el dígito en la nueva base) y el operador `//` para actualizar el número para la siguiente iteración.
* **Manejo de Hexadecimal**: Para la base 16, utlilice una cadena de referencia `"0123456789ABCDEF"`. Esto permite que residuos como `10` o `15` se mapeen automáticamente a las letras `A` o `F` usando el índice de la cadena.

Orden de los Dígitos
los residuos se obtienen de derecha a izquierda. Para resolver esto, en la línea `resultado = digitos[residuo] + resultado`, utilice el nuevo dígito **al principio** de la cadena, eliminando la necesidad de usar una función `reverse()` al final.

Adherecionnno de Métodos Públicos
Finalmente, puse métodos simples como `a_binario()` o `a_hexadecimal()`. Estos actúan como "envoltorios" que llaman al método interno con la base específica, haciendo que el uso de la clase sea facil de usar para cualquier usuario.
