
'''
def addTwo(a,b) : # 2개 정수를 덧셈 후 반환
     return a+b

def addFive(a,b,c,d,e) : # 5개 정수를 덧셈 후 반환
    return a+b+c+d+e

def addThree(a,b,c) : # 3개 정수를 덧셈 후 반환
    return a+b+c

#------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수(1)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data )
# - 가변 인자 함수
# - 매개변수 갯수 : 0개 ~ N개
#--------------------------------------------------


def add_num(*data) :
    ret=0
    for d in data :
        ret+=d
    return ret
print(add_num(1,2,3,4,5))


print(add_num(*range(1,11)))

a=[11,22,33,44]
print(a)
print(*a,sep="-")
aTuple='a','b','c'
print(*aTuple,sep="-")
'''

aDict={'jj':'Hong','age':100}
print(*aDict, sep='-') # 키값을 추출할 수 있다
#print(**aDict, sep='-') **두개짜리를 쓸 수 없다

