# # 객체 && class
# price => int/float
# name => strheight =>float
# coffee=>coffeeName = str, coffeePrice = int hasShot = bool
# (struct 구조체[변수모음 = 명사/상태]+ funtion 함수[동사/ 동작]) => classmethod
# coffee=>coffeeName = str, coffeePrice = int hasShot = bool
# Coffee => addshot() addsyrup(),...
#
# 어떤 프로그램인지 미리 계획이 완성 되어야 클래스를 만들 수있습니다.
#     펫보험 dog클래스
# dog => master, name,age, bread,surgeryList, hasAdopt
# dog => changeMasterName,addAge, addSurgery
# 강아지 키우기 dog클래스
# dog=> hp, skill energy, state
# dog =>takeAwalking

class Car:
    #생성자 함수
    def __init__(self,b,n,c):
        self.brand = b
        self.name = n
        self.color = c
    def introduce(self):
        print(f"차의이름은 {self.name} 브랜드는 {self.brand} 차 색깔은 {self.color}")

    def horning(self):
        print("빵빵 경적을 울립니다~")

    def driving(self):
        print("부릉부릉 앞을 갑니다")

a = Car('현대', 'k5', '검은색')
print(a)
a.introduce()

#절차 지향 프로그래밍 -> 객체지향 프로그래밍(OOP)
절차 [연산자 지향] 지향 (위에서 아래로
유지 보수 힘듬 / 결과 예측불가

객체 [object 지향] 지향() object

