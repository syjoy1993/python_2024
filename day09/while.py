#while  반복문
# 조건식이 특정 탈출 경우가 없으면 무한 루프 빠짐!


# while 첫번째 사용법
# a = 1
# while a < 10:  # 조건문
#     print('아메리카노')
#     a += 1
# 이럴꺼면... for쓰징,


while True:
    print("너가 숫자 1을 넣어야 탈출가능")
    num = int(input("숫자 입력:"))
    if num == 1:
        break


# for와 while의 차이
#
# while: 유저가 끝을 결정짓는 상황
# for: 프로그래머가 끝을 결정짓는 상황

coffeeList = []  # 데이터 베이스, 엑셀에서 가져오는 코드를 넣음

while True: #주로 많이 씀
    print("메가커피 프로그램")
    print("1. 커피등록하기")
    print("2. 커피메뉴보기")
    print("3. 시스템 종료")
    codeNumber = int(input("번호 입력:"))
    if codeNumber == 1:
        print("커피 등록 시스템")
        coffeeName = input("커피이름입력:")
        coffeeList.append(coffeeName)
        print("등록완료!")
    elif codeNumber == 2:
        if len(coffeeName) == 0:
            print("커피메뉴가  없어요. ")
        else:
            print(coffeeList)

    elif codeNumber == 3:
        print("이용해주셔서 감사합니다")
        break

    else:
        print("")