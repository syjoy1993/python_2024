import ccxt
exchange = ccxt.binance()
ticker = exchange.fetch_ticker('BTC/USD')
current_price = ticker['last']
print(f"BTC/USD의 현재 가격:{current_price}")

prev_price = current_price


while True:
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker('BTC/USD')
    current_price = ticker['last']
    print(f"BTC/USD현재가격: {current_price}")

    #1$ 오르면 한걍뷰 가자
    #1$ 떨어지면 돔황챠
    if prev_price - current_price > 0: # 떨어지면 양수
        print("제발 돔황챠")
    else:
        print("한강뷰 가즈아")
    prev_price = current_price # 재갱신
