#-----------------------------------------------------------
# List 자료형의 연산 살펴보기
# - 산술연산
# - 비교연산
# - 멤버연산자
#------------------------------------------------------------
'''
#1~50 범위의 2의 배수로 구성된 리스트 생성
twoNums=list(range(2,51,2))

# 산술연산 => 덧셈(+), 곱셈(*) --------------------------------
print(twoNums + ["A","B"])
datas=twoNums + ["A","B"]
print(datas)
#datas=twoNums + "ABC"   # list는 str과 합칠 수 없다
#                        # 덧셈연산은 list와 list의 합만 된다
print(twoNums + list("ABC")) # 덩어리로 들어가지 않고 따로 떨어져서 들어간다
#list + str => str(list) + str
print(str(twoNums)+ "ABC") #이상하게 나온다
aa=str(twoNums)
print(aa[0])
'''

twoNums=list(range(2,51,2))
datas=twoNums + ["A","B"]

#list * int => int 만큼 원소를 반복해서 하나의 list
print(twoNums*3)

# 멤버 연산 => in / not in ----------------------------------
# => 결과 : True, False
print("C" in datas )
print( 2 in datas )

