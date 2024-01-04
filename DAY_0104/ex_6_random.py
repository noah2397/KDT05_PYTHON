#-------------------------------------------------------------
# 모듈(Module) : 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# - 예 : 수학관련 변수, 함수, 클ㄹ래스 => math.py
#        파이썬 기본제공 변수, 함수, 클래스 => builtin.py
# - 사용법 : import 모듈명
# - 모듈의 기능 사용법 : 모듈병.변수명
#                   : 모듈명.함수명()
#--------------------------------------------------------------
# 사용하고 싶은 변수, 함수, 클래스가 있는 모듈 포함
import random
import math
'''
print(math.pi)
print(math.factorial(5))

# 0.0 <= x < 1.0 사이의 임의의 실수 추출 => random() 함수
for cnt in range(10):
    print(random.random())

# 0.0 <= x < 9.0 사이의 임의의 실수 추출 => random() 함수
for cnt in range(10):
    print(int(random.random()*10))

# 1.0 <= x <= 10.0 사이의 임의의 실수 추출 => random() 함수
for cnt in range(10):
    print(int(random.random()*10)+1)

# a <= x <= b 사이의 임의의 정수 추출 => randint() 함수
for cnt in range(10):
    print(random.randint(1,10),end=("," if cnt!=9 else ""))
'''

lotto_set=set()
while True :
    if len(lotto_set)==6 :
        break
    lotto_set.add(random.randint(1,45))
print(sorted(lotto_set))

lotto_set=[]
while True:
    if len(lotto_set)==6 :
        break
    num=random.randint(1,45)
    if num not in lotto_set :
        lotto_set.append(num)
print(sorted(lotto_set))