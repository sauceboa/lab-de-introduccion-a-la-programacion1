
from flask import Flask, Response, render_template_string, jsonify
import cv2
from pyzbar.pyzbar import decode

app = Flask(__name__)

# Variable global renombrada
scanned_info = ""

# Iniciar la cámara
camera = cv2.VideoCapture(0)

def process_video_feed():
    global scanned_info

    while True:
        success, img = camera.read()

        if not success:
            continue  # Prevenir que el stream se caiga

        # Decodificar usando el método importado directamente
        detected_barcodes = decode(img)

        for barcode in detected_barcodes:
            # Extraer puntos del polígono/rectángulo
            (x, y, w, h) = barcode.rect

            # Dibujar rectángulo azul (B, G, R) en lugar de verde, y un poco más grueso
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

            # Obtener datos y tipo
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # Formatear el texto de forma diferente
            formatted_text = f"[{barcode_type}] {barcode_data}"
            scanned_info = formatted_text

            # Cambiar la fuente, color (azul) y posición del texto
            cv2.putText(img, formatted_text, (x, y - 15),
                        cv2.FONT_HERSHEY_DUPLEX, 0.5,
                        (255, 0, 0), 1)

        # Codificar a formato JPEG
        success_encode, jpeg_buffer = cv2.imencode('.jpg', img)

        if not success_encode:
            continue

        frame_bytes = jpeg_buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


# Diseño HTML y CSS completamente diferente (Modo oscuro)
html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escáner QR / Barras</title>
    <style>
        :root {
            --primary-color: #007bff;
            --bg-color: #1a1a2e;
            --text-color: #e9ecef;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0;
            padding: 2rem;
        }
        h1 {
            margin-bottom: 20px;
            letter-spacing: 1px;
            color: #00d2ff;
        }
        .video-container {
            border: 3px solid #00d2ff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,210,255,0.2);
        }
        .result-box {
            margin: 20px 0;
            padding: 15px 30px;
            background: #16213e;
            border-radius: 8px;
            border: 1px solid #0f3460;
            min-width: 300px;
            text-align: center;
            font-size: 1.2rem;
            color: #00d2ff;
            font-weight: 600;
        }
        .action-btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 1rem;
            border-radius: 5px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .action-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <h1>Sistema de Escaneo</h1>
    
    <div class="video-container">
        <img src="/stream" width="500" alt="Cámara">
    </div>

    <div class="result-box" id="data-output">Esperando lectura...</div>

    <button class="action-btn" onclick="copyData()">Copiar al portapapeles</button>

    <script>
        // Lógica de copiado con bloque try/catch
        async function copyData() {
            const textElement = document.getElementById("data-output");
            const textToCopy = textElement.innerText;

            if (textToCopy === "Esperando lectura...") {
                alert("Aún no se ha detectado ningún código.");
                return;
            }

            try {
                await navigator.clipboard.writeText(textToCopy);
                alert("¡Copiado al portapapeles!");
            } catch (err) {
                alert("Fallo al copiar.");
            }
        }

        // Obtener datos usando async/await en lugar de promesas con .then()
        async function fetchScannerData() {
            try {
                const response = await fetch('/get_data');
                const data = await response.json();
                if (data.result) {
                    document.getElementById('data-output').innerText = data.result;
                }
            } catch (error) {
                console.error("Error obteniendo datos:", error);
            }
        }

        // Consultar cada 800ms en lugar de 500ms
        setInterval(fetchScannerData, 800);
    </script>
</body>
</html>
"""

@app.route('/')
def main_route():
    return render_template_string(html_template)

@app.route('/stream')
def stream_route():
    return Response(process_video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_data')
def get_data_route():
    return jsonify({"result": scanned_info})

if __name__ == "__main__":
    app.run(debug=True)
