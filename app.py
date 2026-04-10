from flask import Flask, request, jsonify
import pandas as pd
from strategy import generate_signals
from backtest import backtest
from metrics import metrics

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor activo 🚀"

@app.route("/backtest", methods=["POST"])
def run_backtest():
    file = request.files["file"]
    df = pd.read_csv(file)

    df = generate_signals(df)

    final_balance, trades = backtest(df)

    result = metrics(trades, 10000, final_balance)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)