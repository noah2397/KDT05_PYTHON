# 코딩도장 p.219 심사문제

num=int(input())

for i in range(num) :
    print(" "*(num-i-1),end="")
    print("*"*(2*(i+1)-1))