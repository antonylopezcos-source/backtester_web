def metrics(trades, initial_balance, final_balance):
    wins = [t for t in trades if t > 0]
    losses = [t for t in trades if t <= 0]

    winrate = (len(wins) / len(trades)) * 100 if trades else 0

    gross_profit = sum(wins)
    gross_loss = abs(sum(losses))

    profit_factor = gross_profit / gross_loss if gross_loss != 0 else 0

    return {
        "trades": len(trades),
        "winrate": round(winrate, 2),
        "profit_factor": round(profit_factor, 2),
        "net_profit": round(final_balance - initial_balance, 2)
    }