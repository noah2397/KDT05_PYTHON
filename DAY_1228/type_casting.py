"""
타입 캐스팅(Type Casting) / 형변환
- 정수 => 실수, 정수=> 문자열, 정수 => 논리
  다른 데이터 타입으로 변환하는 것
- 함수 : 데이터 타입명()
 => 정수 형변환 해주는 함수  int()
    실수 형변환 해주는 함수  float()
    문자열 형변환 해주는 함수  str()
    논리 형변환 해주는 함수   bool()
"""
'''
# int 데이터 타입으로 형 변환-------------------------
# int( 데이터 )
print(type(int('200')))
print(int(200.4),type(int(200.7)))  # float을 int로 변환 => 0.7이라는 데이터 손실이 일어난다
# 붕어빵 틀에 팥이나 슈크림을 넣냐에 따라 달라진다, 붕어빵 틀은 생성자 함수라고 한다, 클래스 이름과 똑같다
# int 그 자체는 정수를 담을 수 있는 틀이다. 클래스
# int()는 정수를 담을 수 있게 해주는 메서드, 즉 생성자 함수이다

print(type(int('200.4')))  # float문자열을 int로 변환 =>십진수로 변환되지 않는 데이터기에 변환되지 않고 오류 방출
print(type(int('200Day'))) # 문자가 포함된 문자열은 int로 변환 => 십진수로 변환되지 않는 데이터기에 변환되지 않고 오류 방출


value=int('200')#계속 사용할 것 같으면 다음과 같이 변수에 값을 할당하자
type(value)

#임베디드 시스템을 만들때는 변수가 작다. 사용할 수 있는 메모리가 작기 때문
'''

'''
#bool => int
# => 0, 1 => False, True
print(type(int(False)), int(False), type(False))
print(type(int(True)), int(True), type(True))
#print(type(int("True")), int("True")) # 이것 역시 str타입을 int로 바꾸려니 오류가 난다

# float 데이터 타입으로 형 변환-------------------------
# str => float('0~9, .')
print( type( float('3.5')), float('3.5') )
print( type( float('35')), float('35') )
print( type( float('-35')), float('-35') )

# int => float
print( type(float(45)), float(45))
print( type(float(-45)), float(-45))

#bin => float
print( type( float(0x123)), float(0x123) )

#bool => float
print( type(float(False)), float(False) )
print( type(float(True)), float(True) )
'''


