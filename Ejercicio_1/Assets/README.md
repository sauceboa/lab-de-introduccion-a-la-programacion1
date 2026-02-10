Este documento describe el procedimiento completo para trabajar el laboratorio de introducción a la programación desde cero. 
Primero se debe contar con Python 3, un editor de código como Visual Studio Code y una terminal. 

Una vez dentro del proyecto, se crea un entorno virtual para trabajar de forma aislada ejecutando el comando `python3 -m venv venv`. 
Al terminar la creación del entorno virtual, se procede a activarlo; en sistemas Linux o Mac se utiliza el comando `source venv/bin/activate`,
mientras que en Windows se usa `venv\Scripts\activate`. 

Cuando el entorno virtual está activo, la terminal mostrará `(venv)` al inicio de la línea.

A continuación se debe configurar el intérprete de Python en el editor de código para que apunte al entorno virtual creado, como se muestra en la siguiente imagen:  
<img width="763" height="207" alt="interpreter" src="https://github.com/user-attachments/assets/500f2b7f-1791-44e2-8bc4-b12d5bd325ca" />

Después de configurar el intérprete correctamente, se instala la librería necesaria para el ejercicio utilizando el comando `pip install numpy`, 
lo cual permite trabajar con arreglos y operaciones numéricas; el proceso de instalación puede verse en la siguiente imagen:  
<img width="907" height="257" alt="numpy" src="https://github.com/user-attachments/assets/1577e6a5-5b4f-4e19-8d29-498f174c2c01" />



También es importante verificar que el editor esté usando el intérprete correcto del entorno virtual, como se observa en la siguiente imagen:  
<img width="756" height="62" alt="venv" src="https://github.com/user-attachments/assets/0c4bccc2-f22a-4013-a221-1e9895751229" />


Una vez configurado el entorno, se crea un archivo llamado `ejercicio1.py` y dentro de él se copia el siguiente código:
```python
import numpy as np
numeros = np.array([1, 2, 3, 4])
print(numeros)
