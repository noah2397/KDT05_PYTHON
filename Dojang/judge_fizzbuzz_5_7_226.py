# 코딩도장 p.226 심사문제

num1, num2= map(int, input().split())
for i in range(num1, num2+1) :
    print("Fizz"*(i%5==0) + "Buzz"*(i%7==0) or i)