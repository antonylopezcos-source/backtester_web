import pandas as pd

def generate_signals(df):
    df['ema_fast'] = df['close'].ewm(span=9).mean()
    df['ema_slow'] = df['close'].ewm(span=21).mean()

    df['signal'] = 0
    df.loc[df['ema_fast'] > df['ema_slow'], 'signal'] = 1
    df.loc[df['ema_fast'] < df['ema_slow'], 'signal'] = -1

    return df