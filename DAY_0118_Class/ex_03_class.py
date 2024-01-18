#----------------------------------------------------------------------------------
# 사랑 클래스 ( 이성간의 사랑 )
# 클래스 이름 : Love
# 클래스 속성 : kind
# 클래스 기능 : 새우까주기, 깻잎떼주기, 금융치료하기, 데려다주기, 데이트하기, 같이아프기
#              대신죽어주기, 희생하기
#-----------------------------------------------------------------------------------

'''
class Love:
    def __init__(self, kind="일반적 사랑"):
        self.kind=kind
    def saeukkajugi(self, saeu=1, kkaneun_sokdo=1 ):
        print(f'당신의 애인이 새우 {saeu}개를 분당 {saeu/kkaneun_sokdo}의 속도로 까주고 있습니다!')
    def kkaesipttejugi(self,kkaesip=1, ttejuneun_sokdo=1  ):
        print(f'당신의 애인이 깻잎 {kkaesip}개를 분당 {kkaesip / ttejuneun_sokdo}의 속도로 떼주고 있습니다!')
    def geumyungchiryohagi(self, don="10000"):
        print(f'돈 {don}원을 받았습니다! 야호!')
    def deryeodajugi(self, eodiro="어디든지"):
        print(f'{eodiro}로 애인이 데려다줬습니다. 신나~')
    def deiteuhagi(self):
        print("애인과 데이트를 했습니다")
    def gatiapeugi(self):
        print("...")
    def daesinjugeojugi(self):
        print("실화야?")
    def huisaenghagi(self):
        print("희생하기")


'''
#----------------------------------------------------------------------------------
# 계산기 클래스
# 클래스 이름 : Cal
# 클래스 속성 : 브랜드, 종류(일반, 공학용), 색깔, 크기
# 클래스 기능 : 덧셈, 뺄셈, 곱셈, 나눗셈
# - 데이터 => 속성 또는 기능에서 매개변수
#-----------------------------------------------------------------------------------

class Calc:
    #클래스 변수
    maker='kasio'
    __size=(7,15)
    def __init__(self, kind, color, price, info):
        self.kind=kind
        self.color=color
        self.price=price
        self.__info=info # 각인시키기
        self.data=0 # 계산 결과 초기값

    def plus(self,nums):
        self.data += nums
    def minus(self,nums):
        self.data -= nums
    def multi(self,nums):
        self.data *= nums
    def div(self,nums):
        if not nums :
            return '0으로 나눌 수 없습니다'
        self.data/=nums
    def result(self):
        return self.data



    def setinfo(self, info):
        self.__info=info
    def getinfo(self, info):
        return self.__info
    # 비공개 인스턴스 속성 읽기/쓰기(getter/setter) 메서드 => 속성 읽기/쓰기 방식으로 동작하도록 설정
    # 더럽게 getter/setter 메서드 쓸 필요 없이 일관적 사용 가능
    @property
    def info(self):
        return self.__info
    @info.setter
    def info(self,info):
        self.__info=info


c1=Calc('공학용','블랙','10x20',"명노아")
print("info : ", c1.info) # 마치 속성 읽듯이 읽지만, __info라는 비공개 인스턴스를 읽어들이고 있는 것이다
c1.info=3
print("info : ", c1.info)