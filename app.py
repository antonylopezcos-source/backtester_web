from flask import Flask, request, jsonify
import subprocess
import json

from flask import Flask, request, render_template_string
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Backtester XAUUSD</title>
</head>
<body style="background:#0f172a; color:white; text-align:center; font-family:sans-serif;">

from flask import Flask
import subprocess

app = Flask(__name__)

# =========================
# 🧩 FRONTEND SIMPLE
# =========================
@app.route('/')
def home():
    return '''
    <h1>Backtester XAUUSD</h1>
    <button onclick="runStrategy()">Ejecutar Estrategia</button>
    <pre id="output" style="background:#111;color:#0f0;padding:10px;"></pre>

    <script>
    function runStrategy() {
        document.getElementById('output').innerText = "Ejecutando estrategia...";

        fetch('/run', { method: 'POST' })
        .then(res => res.text())
        .then(data => {
            document.getElementById('output').innerText = data;
        })
        .catch(err => {
            document.getElementById('output').innerText = "Error: " + err;
        });
    }
    </script>
    '''

# =========================
# 🚀 BACKEND (EJECUTA TU BOT)
# =========================
@app.route('/run', methods=['POST'])
def run():
    try:
        result = subprocess.check_output(
            ["python", "main.py", "--synthetic", "--bars", "100000", "--strategy", "ema_cross"],
            stderr=subprocess.STDOUT
        )
        return result.decode('utf-8')
    except Exception as e:
        return f"Error ejecutando estrategia:\\n{str(e)}"


# =========================
# 🔥 CORRER EN RENDER
# =========================
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)