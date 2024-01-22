# abstract
# 추상 클래스
# 개
# 사전상 '개'
# 내가 키우는 '개'
# 점점 속성들을 명명 해서 구체화 시킬 수 있음

from abc import ABC, abstractmethod  # 추상 클래스 모듈 불러오기, ABCㄱㅏ 추상클래스라고 말해줌

class Shape(ABC): # 물려받음
    @abstractmethod # 아직 정의는 안했는데 어떤 동작을 시킬꺼야
    def get_area(self):
        pass

    @abstractmethod
    def get_round(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius ** 2
    def get_round(self):
        return  3.14 * self.radius * 2

class Triangle(Shape):
    def __init__(self,a,b,c,h):
        self.a = '변의 길이 a'
        self.b = '밑변의 길이 b'
        self.c = '변의 길이 c'
        self.h = 'height'

    def get_areaTriangle(self):
        return self.b * self.h * 0.5

    def get_roundTriangle(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Shape):
    def __init__(self,b,h):
        self.base = b
        self.height = h

    def get_area(self):
        return self.base * self.height * 0.5

    def get_round(self):
        return self.base * 3
class EquilateralSquale(Shape):
    def __init__(self,a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def get_round(self):
        return self.a * 4

# 사용
a = EquilateralTriangle(5,8)
# 값 넣어줘야함

print(a.get_area())
print(a.get_round())

b = EquilateralSquale(9)
print(b.get_area())
print(b.get_round())




