#library....없는거 쓸때 설치해야됨
# 모듈 오픈소스 없을때
import yfinance

apple = yfinance.Ticker("AAPL") #AAPL 애플 주식 심볼
current_price = apple.info['currentPrice']
print(f'애플 주식의 현재 가격: {current_price}')



MS = yfinance.Ticker("MSFT") #AAPL 애플 주식 심볼
current_price = MS.info['currentPrice']
print(f'마이크로소프트 주식의 현재 가격: {current_price}')