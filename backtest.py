def backtest(df):
    balance = 10000
    position = 0
    entry = 0
    trades = []

    for i in range(1, len(df)):
        if df['signal'].iloc[i] == 1 and position == 0:
            position = 1
            entry = df['close'].iloc[i]

        elif df['signal'].iloc[i] == -1 and position == 1:
            exit_price = df['close'].iloc[i]
            pnl = exit_price - entry

            balance += pnl * 100
            trades.append(pnl)

            position = 0

    return balance, trades