# [실습1] 2개 숫자 데이터 입력받은 후 2개의 값을 산술연산결과를 출력해주세요
num1, num2=map(int, input().split())  #map으로 타입캐스팅
print(f"{num1}+{num2}={num1+num2}")
print(f"{num1}-{num2}={num1-num2}")
print(f"{num1}/{num2}={num1/num2}")
print(f"{num1}*{num2}={num1*num2}")
print(f"{num1}//{num2}={num1/num2}")
print(f"{num1}**{num2}={num1**num2}")



# [실습2] 실습1에서 입력받은 숫자 데이터를 활용하여 비교연산결과
print(f"{num1}>{num2}={num1>num2}")
print(f"{num1}<{num2}={num1<num2}")
print(f"{num1}>={num2}={num1>=num2}")
print(f"{num1}<={num2}={num1<=num2}")
print(f"{num1}=={num2}={num1==num2}")
print(f"{num1}!={num2}={num1!=num2}")

# [실습3] 입력받은 숫자 데이터를 활용하여 논리연산 결과 출력하세요

max1=int(input("최댓값 : "))
min1=int(input("최솟값 : "))

print(f"{num1}>{num2} and {num1}>{max1} = {num1>num2 and num1>max1}")
print(f"{num1}>{num2} and {num1}>{min1} = {num1>num2 and num1>min1}")
print(f" not {num1} = {not num1}")