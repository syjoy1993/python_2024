
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
# 내가 한거 인듯
# moviesort = [10000, 8000, 9000]
# popcorn = [6000, 5000, 5000]
# movieuser = int(input("영화 종류를 숫자로 입력 [1.액션영화 2.로코 3.공포]")) - 1
#
# userpop = int(input("원하는 팝콘을 숫자로 입력 하세요[1.치즈팝콘 2.캬라멜 3. 일반]")) -1
# #cgv['movie']['movieList'][1] = 1.액션

cgv = {
    'movie': {
        'movieList': ['1.액션', '2.로코', '3. 공포'],
        'moviePrice': [10000, 8000, 9000]
        #엑셀 리슽로 이런걸 받음, 리스트가 바껴도 다 돌아가게 됨
    },
    'popcorn': {
        'popList': ['1.치즈팝콘','2.캬라멜', '3. 일반'],
        'popPrice': [6000, 5000, 5000]
    }
}


print(f"{cgv['popcorn']}을 보여주세요")
print(cgv['movie']['movieList'])

cgv['movie']['movieList']
# dict cgv에 'movie'로 들어가서 그중에 movieList로 들어감

cgv['movie']['moviePrice'] # [10000, 8000, 9000] 선택
cgv['popcorn']['popList'] # ['1.치즈팝콘','2.캬라멜', '3. 일반'] 선택
cgv['popcorn']['popPrice'] # [6000, 5000, 5000] 선택




choiceMovie = int(input(f"영화를 고르세요{cgv['movie']['movieList']}"))-1
choicPopcorn = int(input(f"팝콘를 고르세요{cgv['popcorn']['popcornList']}"))-1

print(f"선택한 영화: {cgv['movie']['movieList'][choiceMovie]}, 선택한 팝콘:{cgv['popcorn']['popcornList'][choicPopcorn]}, 총금액:{cgv['movie']['moviePrice'][choiceMovie] + cgv['popcorn']['popcornPrice'][choicPopcorn]}")

# 우리가 리스트에서 리스트 1개 요소만 선택할때 list[1]이라고 하니까
#선택한 영화가 2.로코 라면 movieList[1] 으로 하면 2. 로코가 선택이 된다.







