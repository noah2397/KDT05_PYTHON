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

