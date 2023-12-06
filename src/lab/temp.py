import ccxt

binance = ccxt.binance()

print(binance.fetch_ticker('BTC/USDT'))