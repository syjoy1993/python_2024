#library....없는거 쓸때 설치해야됨
# 모듈 오픈소스 없을때
import ccxt
exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']
prev_price = current_price

while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"BTC/USD현재가격: {current_price}")
    if prev_price - current_price > 0:
        print("제발 돔황챠")
    else:
        print("한강뷰 가즈아")
    prev_price = current_price


