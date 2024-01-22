# 상속

class BankAccount:
    def __init__(self, account_number,owner_name):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = 0

# 몬스터
class Monster:
    def __init__(self,hp,name,damage):
        self.hp = hp
        self.name = name
        self.damage = damage

    def attack(self, character):
        character.hp -= self.damage
        # 지금 공격력에서 공격하면 self의 데미지 만큼 빼줄꺼임

class Slime(Monster): ## Monster상속
    # 초기화 해주자__init__으로
    def __init__(self,hp,name,damage,poison):
        super().__init__(hp,name,damage)
        # 부모에 있는 "__init__(self,hp,name):"을 줄테니 실행해 주세요우
        self.poison = poison
        # 자식인 slime의 자기 생성자

    #  부모요소에 있던것을 슬라임에게 조금 다르게 줄꺼임 = 재정의
    # => 이것을 오버라이딩이라고 한다.
    # 자식클래스가 부모 클래스로부터 상속 받은 매서드를 자신의 필요에 맞게 재정의
    # 상속받은 기능 유지 + 특정부분 사짓에게 맞게 커스터마이징함
    
    def attack(self, character):
        character.hp -= self.damage * 2


    def sprayPoison(self, character):
        character.hp -= self.damage + self.poison
        # 독뿌리기 공격할껀데 부모 요소의 monster에서 공격하면 self에서 데미지만큼 빼주는데,
        # 데미지와 독까지 뺴줘야함
# kim = Character() kim이라는 캐릭토

a= Slime(50,'귀여운 슬라임', 30,5)
# a.attack(kim)
# a.sprayPoison(kim)
# kim이라는 캐릭터를 공격하면 빠짐