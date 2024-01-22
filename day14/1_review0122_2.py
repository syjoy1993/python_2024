
# 은행계좌 관리 시스템
# while문 사용 계속해서 사용자의 입력을 받고 적절한 기능을 수행할 수 있도록 해야한다
# 사용자가 프로그램을 종료하기전까지 계속해서 동작할 것
#
from functools import reduce
class BankAccount:
    def __init__(self,account_number,owner_name,balance):
         self.account_number = []
         self.owner_name = []
         self.balance = []



        #  self.account_info = {
    #                           1: account_number,
    #                           2: owner_name,
    #                           3: balance
    #                           }안되나용?


    def deposit(self,account_number):  #입금

        account_number = int(input("계좌번호를 입력하세요"))
        check = input(f'예금주 확인 {myAccount.owner_name[myAccount.account_number.index(account_number)]} 맞으면 1 틀리면 아무 숫자나 누르세요')
        if check == 1: # 이하가 실행이 안되는 이유는..?
            deposit_money = int(input("입금할 금액을 입력하세요."))
            if deposit_money > 0:
                self.balance.append(deposit_money)
            else:
                pass
        else:
            pass

        return print(f"잔액은{reduce(lambda x,y:x+y, self.balance)}입니다")
        # self.balance,금액 합산이 안됨 #self.balance += deposit_money 왜 안될까여
        # if문에 쓰는것?



    def withdeaw(self,account_number,withdeaw_money): # 출금


        if reduce(lambda x,y:x+y, self.balance) >= withdeaw_money > 0:
            true = int(input(f'출금할 금액은{withdeaw_money}입니까 맞으면 1번 틀리면 아무번호나 누르세요'))
            if true == 1:
                self.balance.append(-withdeaw_money)


            else:
                pass
                print("처음으로 돌아갑니다.")
        else:
            pass
            print("출금 할 금액이 잘못 입력되었습니다. 처음으로 돌아갑니다.")

        return print(f"출금후 잔액은 {reduce(lambda x,y:x+y, self.balance)}입니다.") #if문에 쓰는것?


    def get_balance(self,account_number,owner_name): #잔액
        # reduce()??

        print(f'{self.owner_name[userNum]}님의 {self.account_number[userNum]} 계좌의 현재 잔액은 {reduce(lambda x, y: x + y, self.balance)}원 입니다.')





    def print_account_info(self,account_number): # 계좌 정보


        print(f"해당 계좌번호의 예금주는 {self.owner_name}님 이고, 잔액은 {reduce(lambda x,y:x+y, self.balance)}입니다 ")

myAccount = BankAccount( 0 ,'', 0)
while True:
     UserselctList = ['1.새 계좌 개설', '2.예금', '3.출금', '4.잔액확인', '5.프로그램 종료']
     Userselct = int(input(f"원하시는 옵션을 숫자로 입력하세요{UserselctList}"))

     if Userselct == 1: # 새계좌
         import random

         owner_name = input('당신의 이름을 입력하세요')
         myAccount.owner_name.append(owner_name)

         balance = int(input("입금할 금액을 입력하세요. 없으면 0 입력하세여"))
         myAccount.balance.append(balance)

         account_number = random.randint(10000000000001, 19999999999999)
         myAccount.account_number.append(account_number)

         print(myAccount.owner_name)
         print(myAccount.balance)
         print(myAccount.account_number)

         print(f'{owner_name}님 의 계좌번호는 {account_number}이고, 잔액은 {balance} 입니다.')

     elif Userselct == 2: # 입금

         myAccount.deposit(account_number)


     elif Userselct == 3: # 출금

         account_number = int(input("계좌번호를 입력하세요"))
         withdeaw_money = int(input("출금할 금액을 입력하세요."))
         myAccount.withdeaw(account_number,withdeaw_money)


         # if input(f'예금주 확인{[myAccount.owner_name[myAccount.account_number.index(account_number)]]} 맞으면 1 틀리면 아무 숫자나 누르세요') == 1:
         #
         #    withdeaw_money = int(input("출금할 금액을 입력하세요."))
         #    myAccount.withdeaw(account_number,withdeaw_money)
         #
         # else:
         #     break

     elif Userselct == 4: # 잔액확인
         account_number = int(input("계좌번호를 입력하세요"))
         userNum = myAccount.account_number.index(account_number)
         owner_name = myAccount.owner_name[userNum]

         myAccount.get_balance(account_number, owner_name)

     else:
         break



