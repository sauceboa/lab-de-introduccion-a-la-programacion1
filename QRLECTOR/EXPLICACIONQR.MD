EXPLICACION

Básicamente realizamos una app web con Flask para que la cámara del compu detecte códigos QR o de barras

flask tiene 2 rutas una manda el video (/stream) y otra para consultar el codigo que leyo la camra (/get_data)

OpenCV abre la cámara y va sacando fotos rapidísimo, y Pyzbar se encarga de analizar cada foto para ver si hay un código cuando lo encuentra le pone un recuadro azul al rededor y guarda el contenido en una variable

el video como es video en vivo, lo que hago es convertir cada fotograma a JPG y enviarlo de forma continua al navegador

la pagina la arme minimalista en oscuro y para que los datos aparezcan sin tener que recargar la página, metí un setInterval en JavaScript 

y de ultimas un boton para copiar y pegar 
