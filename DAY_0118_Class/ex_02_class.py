#-----------------------------------------------------
# 자동차 클래스
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성)
#              12   빨강  1111   세단    현대
# 클래스 기능 : 전진한다, 정지한다, 후진한다
#-----------------------------------------------------

class Car:
    maker='현대'

    def __init__(self, wheel, color, number, kind):
        self.wheel=wheel
        self.color=color
        self.number=number
        self.kind=kind

    def driving(self, where="그곳"):
        print(f'{where}에 {self.number} 차가 가고 있습니다!')
    def stop(self, place="주차장"):
        print(f'{self.number}차가 {place}에 멈췄습니다!')
    def back(self):
        print(f'{self.number}차가 후진합니다!')

myCar=Car(19,'red',1111,'세단')
secondCar=Car(20,'hotpink',7777,'SUV')

#-----------------------------------------------------
# 자율주행자동차 클래스
# 클래스 이름 : AutoCar
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성), AI소프트웨어
#              12   빨강  1111   세단    현대
# 클래스 기능 : 전진한다, 정지한다, 후진한다
#-----------------------------------------------------
class AutoCar(Car):
    def __init__(self, wheel, color, number, kind, AI_software) :
        super().__init__(wheel, color, number, kind)
        self.AI_software=AI_software

    def auto_driving(self, mode_on=False):
        if mode_on==False:
            print("자율주행 모드가 꺼져있습니다")
        if mode_on :
            print("자율주행 모드를 킵니다")


autocar=AutoCar(30,'red',1111,"세단","Piro")
autocar.auto_driving(True)

#-----------------------------------------------------
# 자율주행비행자동차 클래스
# 클래스 이름 : Car
# 클래스 속성 : 바퀴, 색상, 차번호, 차종류, 제조사(클래스 속성), AI소프트웨어, fly
#              12   빨강  1111   세단    현대
# 클래스 기능 : 전진한다, 정지한다, 후진한다
#-----------------------------------------------------

class AutoFlyCar(AutoCar):
    def __init__(self, wheel, color, number, kind, AI_software, fly) :
        super().__init__(wheel, color, number, kind, AI_software)
        self.fly=fly

    def fly_driving(self, mode_on=False):
        if mode_on==False:
            print("비행 모드가 꺼져있습니다")
        if mode_on :
            print("비행 모드를 킵니다")


autoflycar=AutoFlyCar(30,'red',1111,"세단","Piro", False)
autoflycar.auto_driving(False)
autoflycar.fly_driving(True)