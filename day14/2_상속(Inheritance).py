# 상속(Inheritance):
# 기존에 있던 클래스에서 있었던 것을 그대로 물려받음
# 코드 중복을 없애고, 확장 할 수 있다

class BankAccount:
    def __init__(self, account_number,owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0

    def deposit(self, amount): # 적금하는 메소드
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("금액을 잘못입력하였습니다.")
            return False

class KakaoBankAccount(BankAccount):
    pass
# BankAccount의 메소드와 속성을 그대로 물려받음



a = KakaoBankAccount()
a.deposit()