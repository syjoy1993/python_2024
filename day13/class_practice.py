# class_Practice
class Dog:
    def __init__(self,n):
        self.hp = 100 # max200
        self.stress = 50 # max 100
        self.name = n

    def eating(self):
        if(self.hp >= 200):
            print('체력이 꽉 찼습니다.')
            print(f'현재 체력은 {self.hp}입니다')
            self.hp = 200
        else:
            self.hp += 50

a = Dog('bana')
a.eating()
a.eating()
a.eating()
a.eating()
a.eating()

