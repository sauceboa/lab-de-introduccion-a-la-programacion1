Este documento describe el procedimiento completo para trabajar el laboratorio de introducción a la programación desde cero. Primero se debe contar con Python 3, un editor de código como Visual Studio Code y una terminal. Para comenzar, se descarga el repositorio desde GitHub ya sea usando la opción “Code → Download ZIP” o clonándolo con el comando `git clone https://github.com/DiegoRO25/Lab-de-introduccion-a-la-programacion.git` y posteriormente entrando a la carpeta del proyecto con `cd Lab-de-introduccion-a-la-programacion`. Una vez dentro del proyecto, se crea un entorno virtual para trabajar de forma aislada ejecutando el comando `python3 -m venv venv`. Al terminar la creación del entorno virtual, se procede a activarlo; en sistemas Linux o Mac se utiliza el comando `source venv/bin/activate`, mientras que en Windows se usa `venv\Scripts\activate`. Cuando el entorno virtual está activo, la terminal mostrará `(venv)` al inicio de la línea. A continuación se debe configurar el intérprete de Python en el editor de código para que apunte al entorno virtual creado, como se muestra en la siguiente imagen:  
![Entorno virtual](https://github.com/sauceboa/lab-de-introduccion-a-la-programacion1/blob/main/Ejercicio_1/Assets/venv.png)  
Después de configurar el intérprete correctamente, se instala la librería necesaria para el ejercicio utilizando el comando `pip install numpy`, lo cual permite trabajar con arreglos y operaciones numéricas; el proceso de instalación puede verse en la siguiente imagen:  
![Instalación de NumPy](https://github.com/sauceboa/lab-de-introduccion-a-la-programacion1/blob/main/Ejercicio_1/Assets/numpy.png)  
También es importante verificar que el editor esté usando el intérprete correcto del entorno virtual, como se observa en la siguiente imagen:  
![Intérprete de Python](https://github.com/sauceboa/lab-de-introduccion-a-la-programacion1/blob/main/Ejercicio_1/Assets/interpreter.png)  
Una vez configurado el entorno, se crea un archivo llamado `ejercicio1.py` y dentro de él se copia el siguiente código:  
```python
import numpy as np
numeros = np.array([1, 2, 3, 4])
print(numeros)
