# 뉴스기사에서 가장 긴 단어 찾기
article = """
"비트코인 제도권 편입"…잡코인은 '버블 붕괴' 유의

현물 ETF 승인은 가상자산 시장에선 미국의 기준금리 인하만큼이나 빅이벤트로 꼽히는 대형 호재다. 그동안 급격한 변동성과 취약한 시세조작 리스크 등으로 홀대받던 가상자산이 명실상부한 투자 상품으로 인정받는 의미를 지녀서다. ETF 상품을 운영하려는 기관투자자의 자금이 몰리게 되면, 관련 시장 규모가 최소 수십조원에서 최대 5경원 수준으로 커질 것이란 관측도 나온다.

아울러 비트코인은 오는 4월 반감기를 앞두고 있다. 4년마다 한 번씩 오는 비트코인 반감기에는 채굴되는 비트코인의 수가 절반으로 줄어들어 희소성을 높인다. 결국 수요는 커지고 공급이 줄어들면 시장 원칙에 따라 가격이 상승할 것이란 예측이다. 홍성욱 NH투자증권 연구원은 "오는 10일까지 비트코인 현물 ETF 승인이 매우 유력하다"면서 "4월 예정된 비트코인 반감기는 비트코인 마케팅에 크게 도움이 될 것으로 보이고 갈수록 기관투자자들의 영향력이 커질 것"이라고 전망했다.

다만 비트코인 현물 ETF 출시 이후 오히려 가격이 조정될 가능성도 거론된다. 시세차익을 노린 매도세가 쏟아져 나올 수 있다는 이유에서다. 암호화폐 분석 플랫폼 크립토퀀트의 훌리오 모레노 리서치 책임자는 "비트코인을 낮은 가격대에 매수한 투자자들은 이미 엄청난 이익을 실현하고 있고, 역사적으로 이 같은 상황에선 가격이 떨어지는 경향이 있다"면서 "현물 ETF 출시를 계기로 차익 실현이 시작된다면 비트코인은 3만2000달러(4200만원)까지 하락할 수 있다"고 전망했다.

연장선에서 비트코인을 제외한 소위 '잡코인'들의 '옥석 가리기'가 이뤄질 가능성도 언급된다. 김민승 코빗 리서치센터 연구위원은 "미국 시장에서 가상자산 현물 ETF가 승인돼 제도권 기관 자금이 유입되면 ETF가 승인된 자산과 그렇지 않은 자산 간 부익부 빈익빈 현상이 생길 수 있다"면서 "지나친 기대 심리로만 가격이 형성된 일부 알트코인들의 버블 붕괴로 이어질 것"이라고 분석했다.
"""
word = article.split(' ')
wordList.sort()
c = list(set(wordList)) # 중복된거 자르고, 리스트화
# 나머지는 오늘...





# 영화 예매 프로그램
# 영화 종류를 나타내는 정수 1~3과 나이를 받고, 각 영화와 가격은 다음과 같이 설정
# 1.액션영화 :10000
# 2.로코 8000
# 3.공포 9000
#
# 팝콘의 종휴
# 1. 치즈팝콘 6000
# 2.캬라멜 5000
# 3. 일반 5000
#총계산 출력
moviesort = [10000, 8000, 9000]
popcorn = [6000, 5000, 5000]
movieuser = input("영화 종류를 숫자로 입력 [1.액션영화 2.로코 3.공포]") - 1
userage = input("나이를 입력하세요")
userpop = input("원하는 팝콘을 숫자로 입력 하세요[1.치즈팝콘 2.캬라멜 3. 일반]") -1
#cgv['movie']['movieList'][1] = 1.액션

cgv = {
    'movie': {
        'movieList': ['1.액션', '2.로코', '3. 공포'],
        'moviePrice': [10000, 8000, 9000]
        #엑셀 리슽로 이런걸 받음, 리스트가 바껴도 다 돌아가게 됨
    },
    'popcorn': {
        'popList': [1.치즈팝콘 2.캬라멜 3. 일반]
        'popPrice': [6000, 5000, 5000]
    }
}

movie_choice = int(input(f"영화를 고르세요 {cgv['movie']['movieList']}")) -1
movie_choice = int(input(f"영화를 고르세요 {cgv['movie']['movieList']}")) -1

print(f"선택한 영화: {cgv['movie']['movieList'][movie_choice]}, 선택한 팝콘{cgv['popcorn']['popList']['popcorn_choice']}, 총 금액{cgv['movie']['movieList']['movie_choice']+ cgv['popcorn']['popList']['popcorn_choice']}")











