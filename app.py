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

    <h1>🔥 Backtester XAUUSD</h1>

    <form method="post">
        <button type="submit">Ejecutar Estrategia</button>
    </form>

    <pre>{{ resultado }}</pre>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    resultado = ""

    if request.method == "POST":
        try:
            result = subprocess.run(
                ["python", "main.py", "--synthetic", "--bars", "100000", "--strategy", "ema_cross"],
                capture_output=True,
                text=True
            )
            resultado = result.stdout
        except Exception as e:
            resultado = str(e)

    return render_template_string(HTML, resultado=resultado)


import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)