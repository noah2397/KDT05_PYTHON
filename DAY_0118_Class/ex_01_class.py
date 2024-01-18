#--------------------------------------------------------------------
# 사용자 정의 클래스
#--------------------------------------------------------------------
# 클래스 정의 : 밤하늘에 떠있는 별을 저장하는 데이터
# 클래스 이름 : Star
# 클래스속성 : 크기, 색상, 밝기, 이름  => 속성(attribute), 필드(field) => 변수
# 클래스기능 : 반짝거린다. 떨어진다 => 함수(function), 메서드(method) => 함수
#_-------------------------------------------------------------------
class Star: # 그냥 만들었다고 해서 메모리 힙에 데이터가 생기지 않는다
        # 클래스 변수/속성/필드 => 해당 클래스 생성된 객체 즉 인스턴스가 공유하는 속성
    timezone='밤'
    __privateValue=77

         #최상위 부모 클래스인 Object로부터 상속받은 함수 즉 메서드
         #형태 : def __xxx__()
         #나의 클래스에 맞도록 수정 후 리모델링해서 사용 => 오버라이딩(overriding)
    def __init__(self, size, color, brightness, name='unknown'):
        print(f'__init__() : {size},{color},{brightness},{name}')
        # 힙 메모리 영역에 저장 => 속성 데이터의 주소 저장
        self.__size=size  # == myStar.size=size
        self.color=color  # == myStar.color=color
        self.brightness=brightness  # == myStar.brightness=brightness
        self.name=name

    # 별 클래스의 기능 => 메서드
    def drop(self):
        print(f"하늘에 {self.name}별이 떨어집니다. 소원 빌어요~!")

    # 비공개 인스턴스 속성에 접근하기 위한 메서드 => getter/setter 메서드
    # 비공개 인스턴스 속성 읽어오는 메서드 get속성명() ==> 속성명
    # 비공개 인스턴스 속성에 값 설정하는 메서드 set속성명(새로운값)
    def getSize(self):
        return self.__size
    def setSize(self, size):
        self.__size=size

    def __inner(self):
        print("나는 비공개 인스턴스")
    @property # 데코레이터 -> 꾸밀 때  쓴다, 메서드 위에 붙는다, 특별한 기능을 준다
              # property는 getter함수임을 알려준다

    @property  # 함수가 이런 기능을 한다고 미리 알려주는거 -> getter
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter # x라는 걸 세팅해주는 함수라고 알려줌 -> setter
    def x(self, value):
        self._x = value

    @x.deleter #-> deleter
    def x(self): # 나중에 불릴때가 따로있다
        del self._x
    # 객체 즉 인스턴스 생성없이 사용하는 메서드를 넣고싶다!
    @staticmethod
    def add(a,b):
        pass
    @classmethod
    def cc(cls): # 클래스 정보가 자동적으로 들어간다(__dict__에 있는 내용들)
        pass


class Love:
    @staticmethod
    def smile():
        print("hello")
m=Love()
m.smile()
Love.smile()

Star.drop()
myStar=Star(10,"red",20,"벤츠")


# 인스턴스 속성에 간접 접근 => 메서드 제공 필수



#---------------------------------------------------------------------
# 객체 생성 => 클래스에 정의된 속성 즉 변수와 함수들이 메모리 힙 영역에 생성
# 생성 방법 => 클래스명() <- 생성자 함수/메서드
#             클래스명(매개변수1) 생성자 함수/메서드
#             클래스명(매개변수1, 매개변수2, ..., 매개변수N) 생성자 함수/메서드
#---------------------------------------------------------------------

'''
if __name__ == '__main__':
    myStar=Star(5, "dark_yellow",10) # 힙 영역에 만들어졌고, 스택에서 myStar의 주소를 저장하고 있다
    yourStar=Star(10,"red",20, "RedStar")
    yourStar.drop()

#---------------------------------------------------------------------
# 객체의 속성 정보 읽기 => 객체변수명.속성명
#---------------------------------------------------------------------
    print(myStar.brightness)

#---------------------------------------------------------------------
# 객체의 속성 정보 변경 => 객체변수명.속성명 = 새로운 값
#---------------------------------------------------------------------
    myStar.brightness=7
    print(myStar.brightness)
    print(myStar.__dict__)
    print(Star.__dict__)
    print(myStar.timezone)
'''