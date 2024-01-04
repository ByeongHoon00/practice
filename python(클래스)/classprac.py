# init은 생성자로 함수에 정의된 self를 제외한 갯수만큼 전달받아야 객체 생성가능
## class내에 정의된 self.변수들은 모두 멤버변수
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력{1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("빼앗은 레이스", 80, 5)
## class외부에서 변수 확장가능(확장한 객체에 대해서만 적용)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

