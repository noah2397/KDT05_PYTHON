# 코딩도장 p.447 심사문제

class Annie:
    def __init__(self, physical, mana, ap):
        self.physical=physical
        self.mana=mana
        self.ap=ap
    def tibbers(self):
        print(f'티버 : 피해량 {self.ap * 0.65 + 400}')
health, mana, ability_power=map(float, input().split())
x=Annie(health, mana, ability_power)
x.tibbers()

# 1803.68 1184.0 645