
movieList = ['액션영화', '로코', '다큐']
price1 = [12000,10000,11000]
snackPack = ['팝콘세트', '스낵콤보','건강 팩']
price2 = [6000,8000,7000]
upGrade= ['일반좌석', '프리미엄', 'vip']
price3 = [0,5000,10000]
# discount age< 18: 20%할인, age <= 65 ,15%할인
#
# 나이, 종류,스낵팩,좌석 업글

moviePrice = {i+1:{'영화종류':m, 'price1':p} for i,(m,p) in enumerate(zip(movieList,price1))}
snackPackPrice = {i+1:{'snackpack':s,'price2':p} for i,(s,p) in enumerate(zip(snackPack,price2))}
upGradePrice = {i+1:{'seat':u,'price3':p} for i,(u,p) in enumerate(zip(upGrade,price3))}


cgv = {
    1: moviePrice,
    2: snackPackPrice,
    3: upGradePrice
}

# cgv 딕셔너리를 만들었음, 이제 제시문 보여주고 입력받기

userChoice = int(input(f"영화 1.액션영화 2.로맨틱 코메디 3.다큐멘터리  를 골라주세여"))
userChoice2 = int(input(f"snack pack 1.팝콘세트 2.스낵콤보 3.건강팩"))
userChoice3 = int(input(f"좌석을 업그레이드 할까요? 1.일반좌석 2.프리미엄 3.VIP"))


#선택헤서 계산하기
print(f"선택한 영화{cgv[1][userChoice]['영화종류']}, 선택한 snack pack{cgv[2][userChoice2]['snackpack']}, 선택한 좌석{cgv[3][userChoice3]['seat']} 입니다")
totalprice = (cgv[1][userChoice]['price1'] + cgv[2][userChoice2]['price2'] + cgv[3][userChoice3]['price3'])

userAge = int(input(f"나이를 선택하세요 1. 12세 미만 2. 65세이상 3. 13세~64세"))
if userAge == 1:
    totalprice * 0.8
    print(f" 총금액은{totalprice * 0.8}입니다")


elif userAge == 2:
    totalprice * 0.85
    print(f" 총금액은{totalprice * 0.85}")

else:
    totalprice
    print(f" 총금액은{totalprice}")
