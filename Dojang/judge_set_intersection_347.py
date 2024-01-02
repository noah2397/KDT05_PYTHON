# 코딩도장 p.347 심사문제
num1, num2 = map(int, input().split())
a=set()
b=set()

# 1부터 입력받은 수까지 반복하여 약수를 찾음
for i in range(1, num1 + 1):
    if num1 % i == 0:
        a.add(i)
for i in range(1, num2 + 1):
    if num2 % i == 0:
        b.add(i)

divisor= a & b
result=0
if type(divisor) == set :
    result = sum(divisor)
print(result)