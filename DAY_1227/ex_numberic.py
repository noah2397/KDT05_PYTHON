'''
수치 데이터 살펴보기
- 정수 => class int
- 실수 => class float
- 복소수 => class complex
'''

# 0b1010
# 0o127
# 0x8ff
# 1+3j

#--------------------------
# [실습] 2개 정수를 입력 받기
# -> input() 함수 2개 사용
# -> str => int 타입 캐스팅
#--------------------------

num1=int(input())
num2=int(input())

# 비교 연산 결과 출력 -------------------
# [출력] 10>3 => True
print(f"{num1} > {num2} -> { num1 > num2 }")
print(f"{num1} < {num2} -> { num1 < num2 }")
print(f"{num1} >= {num2} -> { num1 >= num2 }")
print(f"{num1} <= {num2} -> { num1 <= num2 }")
print(f"{num1} == {num2} -> { num1 == num2 }")
print(f"{num1} != {num2} -> { num1 != num2 }")








