#-----------------------------------------
# 함수와 클래스
#-----------------------------------------
# 변수에 어떤 데이터를 저장하고 있는지 확인 함수 => type(변수명)
'''
data=1
print(f'dataType => {type(data)}')

data='Good'
print(f'dataType => {type(data)}')

# 함수명의 타입
print(f'id() Type => {type(id)}')

# 함수 종류에는 기본으로 내장되어있는 내장함수와 사용자 정의 함수가 있다
# 사용자 정의 함수 생성--------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출력
# 함수 이름 : addTwo
# 매개 변수 : n1,n2
# 함수 결과 : 없음
#---------------------------------------------
def addTwo(n1,n2) :
    print(f'{n1}+{n2}={n1+n2}')

print(type(addTwo)) # 클래스가 function임을 알 수 있다, 클래스 객체

#-----------------------------------------------------------
# 변수와 함수
# 결국은 파이썬은 모든 게, 클래스다
# 즉 우리가 만든 함수도 클래스에서 나온 객체이다
# - 함수명은 코드의 시작 주소를 저장하고 있음
# - 함수명을 변수에 대입 가능
#-----------------------------------------------------------

test=addTwo # 변수에 함수명을 할당

print(f'test => {id(test)}, {type(test)}')
print(f'addTwo => {id(addTwo)}, {type(addTwo)}')

print(f'test(1,2) => {test(1,2)}')


#-------------------------------------------
# [ 활용예 ]
# - 1~10 범위에서 임의의 정수 5개를 저장
# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값, 합계, 갯수 결과 출력
# - 중복된 정수 가능
#-------------------------------------------
import random

def ranNum():
    result = [random.randint(1,10) for _ in range(5)]
    print(max(result), min(result), sorted(result, reverse=True), sum(result), len(result),"\n")
    func=[max,min,sorted,sum,len] # 여러개의 함수이름을 변수에 저장 => 리스트 사용
    for f in func :
        print(f(result) if f!=sorted else f(result,reverse=True))# default 매개변수

print(ranNum())
'''

#---------------------------------------------
# 키와 출력값을 묶어서 같이 출력하기
#---------------------------------------------
import random


def ranNum():
    result = [random.randint(1,10) for _ in range(5)]
    func=[max,min,sorted,sum,len] # 여러개의 함수이름을 변수에 저장 => 리스트 사용
    func_keyword=["최댓값","최솟값","정 렬","합 계","갯 수"]
    func_dict=dict(zip(func,func_keyword))
    for key, value in func_dict.items() :
        print(f'{value:3} : {key(result) if key!=sorted else key(result,reverse=True)}')
print(ranNum())

