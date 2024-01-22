# abstract
# 추상 클래스
# 개
# 사전상 '개'
# 내가 키우는 '개'
# 점점 속성들을 명명 해서 구체화 시킬 수 있음

# abstract
# 추상 클래스
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_round(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius ** 2
    def get_round(self):
        return 3.14 * self.radius * 2

class Triangle(Shape):
    def __init__(self, b,h):
        self.base = b
        self.height = h
    def get_area(self):
        return self.base * self.height * 0.5
    def get_round(self):
        return self.base * 3

class Square(Shape):
    def __init__(self, s):
        self.side = s
    def get_area(self):
        return self.side * self.side
    def get_round(self):
        return self.side * 4

a = Triangle(5,5)
print(a.get_area())
print(a.get_round())

b = Square(7)
print(b.get_area())
print(b.get_round())



