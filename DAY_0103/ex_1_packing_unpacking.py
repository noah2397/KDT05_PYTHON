#----------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
#----------------------------------------------
msg="1 2 3"
# 팩킹 방식(Packing)
msgList=msg.split()
print(msgList[0], msgList[-1])

#언팩킹 방식(Unpacking)
m1,m2,m3=msg.split()
print(m1,m2,m3)

# 다음 구문은 변수 수가 달라서 에러 발생
# m1,m2=msg.split()
# print(m1,m2)


# 변수를 여러 개 생성하는 경우 -------------
age=12
name="Hong"
job="학생"
age1,name1,job1=12,'Hong',"학생"



def myFunc(a,b) :
    return a+b, a-b, a*b, a/b if not b else -1
result=myFunc(10,3)
print(f'덧셈결과 : {result[0]}, 뺄셈결과 : {result[1]}, 곱셈결과 : {result[2]}, 나눗셈결과 : {result[3]}')
plus, minus, multi,div=myFunc(10,3)
print(f'덧셈결과 : {plus}, 뺄셈결과 : {minus}, 곱셈결과 : {multi}, 나눗셈결과 : {div}')
