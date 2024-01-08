#--------------------------------
# filter(함수명, 반복 가능 객체)
# - 조건에 맞는 데이터만 반환
#--------------------------------
# 예) 5초과 10미만 데이터만 추출

from random import randint,random


a=[8,3,2,10,15,7,1,9,0,11]

def check(data):
    '''
    check함수는 True,False를 반환하는 함수여야한다
    :param data:
    :return:
    '''
    return data>5 and data<10

print(list(filter(check,a)))

from functools import reduce
print(reduce((lambda x,y:x+y),a))




