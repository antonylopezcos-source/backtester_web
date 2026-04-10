from flask import Flask, request, jsonify
import subprocess
import json

app = Flask(__name__)

# Ruta básica
@app.route("/")
def home():
    return "Servidor funcionando 🚀"


# 🔥 BACKTEST REAL
@app.route("/backtest", methods=["POST"])
def backtest():

    try:
        # Ejecuta tu comando CLI
        result = subprocess.run(
            ["python", "main.py", "--synthetic", "--bars", "100000", "--strategy", "ema_cross"],
            capture_output=True,
            text=True
        )

        output = result.stdout

        # 🔥 Aquí puedes mejorar el parseo según tu main.py
        # Por ahora devolvemos texto crudo
        return jsonify({
            "status": "ok",
            "output": output
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })