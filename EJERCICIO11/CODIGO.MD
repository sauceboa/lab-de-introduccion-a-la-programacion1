from flask import Flask, Response, render_template_string, jsonify, request
import cv2
from pyzbar import pyzbar

app = Flask(__name__)

ultimo_codigo = ""
historial = []

# Cámara del servidor (PC)
cap = cv2.VideoCapture(0)

def generar_frames():
    global ultimo_codigo, historial

    while True:
        success, frame = cap.read()

        if not success:
            continue

        codigos = pyzbar.decode(frame)

        for codigo in codigos:
            x, y, w, h = codigo.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            datos = codigo.data.decode("utf-8")
            tipo = codigo.type
            texto = f"{datos} ({tipo})"

            if texto != ultimo_codigo:
                ultimo_codigo = texto
                historial.append(texto)

            cv2.putText(frame, texto, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')


@app.route('/')
def index():
    return render_template_string(HTML)


@app.route('/video')
def video():
    return Response(generar_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/guardar_codigo', methods=['POST'])
def guardar_codigo():
    global historial
    data = request.json
    codigo = data.get("codigo")

    if codigo:
        historial.append(codigo)

    return jsonify({"ok": True})


@app.route('/historial')
def get_historial():
    return jsonify(historial)


HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Scanner Pro</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        body {
            font-family: Arial;
            background: #eef2f7;
            text-align: center;
            margin: 0;
        }

        h1 {
            margin-top: 20px;
        }

        button {
            padding: 12px 18px;
            border: none;
            background: #2ecc71;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
        }

        button:hover {
            background: #27ae60;
        }

        #modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
        }

        #modal-content {
            background: white;
            padding: 15px;
            margin: 15% auto;
            width: 90%;
            max-width: 350px;
            border-radius: 12px;
        }

        #video {
            width: 100%;
            border-radius: 10px;
        }

        .container {
            max-width: 400px;
            margin: auto;
        }

        .card {
            background: white;
            padding: 15px;
            margin-top: 20px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }

        .item:last-child {
            border-bottom: none;
        }

        .delete {
            background: #e74c3c;
            padding: 6px 10px;
            border-radius: 6px;
            font-size: 12px;
        }

        .delete:hover {
            background: #c0392b;
        }

        #contador {
            margin-top: 10px;
            font-weight: bold;
            color: #555;
        }
    </style>
</head>

<body>

<div class="container">

<h1>🛒 Scanner Pro</h1>

<button onclick="abrirCamara()">📷 Escanear producto</button>

<div id="contador">Productos: 0</div>

<div class="card">
    <h3>📦 Carrito</h3>
    <div id="historial"></div>
</div>

</div>

<!-- MODAL -->
<div id="modal">
    <div id="modal-content">
        <video id="video" autoplay></video><br><br>
        <button onclick="cerrarCamara()">Cerrar</button>
    </div>
</div>

<script src="https://unpkg.com/@zxing/library@latest"></script>

<script>
let codeReader = new ZXing.BrowserBarcodeReader();
let video = document.getElementById('video');

function abrirCamara() {
    document.getElementById('modal').style.display = 'block';

    codeReader.decodeFromVideoDevice(null, video, (result, err) => {
        if (result) {
            let codigo = result.text;

            fetch('/guardar_codigo', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({codigo: codigo})
            });

            cerrarCamara();
        }
    });
}

function cerrarCamara() {
    document.getElementById('modal').style.display = 'none';
    codeReader.reset();
}

// ELIMINAR PRODUCTO
function eliminar(index) {
    fetch('/eliminar', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({index: index})
    });
}

// ACTUALIZAR UI
function actualizarHistorial() {
    fetch('/historial')
    .then(r => r.json())
    .then(data => {
        let html = "";

        data.forEach((c, i) => {
            html += `
            <div class="item">
                <span>${c}</span>
                <button class="delete" onclick="eliminar(${i})">X</button>
            </div>`;
        });

        document.getElementById("historial").innerHTML = html;
        document.getElementById("contador").innerText = "Productos: " + data.length;
    });
}

setInterval(actualizarHistorial, 800);
</script>

</body>
</html>
"""

@app.route('/eliminar', methods=['POST'])
def eliminar():
    global historial
    data = request.json
    index = data.get("index")

    if index is not None and 0 <= index < len(historial):
        historial.pop(index)

    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context='adhoc')
