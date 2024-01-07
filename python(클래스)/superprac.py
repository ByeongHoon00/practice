# 다중 상속의 경우 super를 사용하면 맨 처음 상속받는 클래스에 대해서만 호출 

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlayableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlayableUnit()