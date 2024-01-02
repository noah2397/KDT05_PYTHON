'''
논리연산자 => and, or, not
- 결과 : True, False
- 동작방식
  * and => A and B 모두 True일 때만 True
  * or  => A or B 둘중에 하나만 True일 때 True
  * not => not A : 현재 A의 상태를 반대로 => not Ture --> False, not False --> True : 토글(toggle)
'''
'''
no1, no2 = 10, 3

# and 연산자----------------------------------------------------
#no1은 no2보다 크고 그리고 100보다 큰 수
print(no1 > no2 , no1 > 100)

print(no1 > no2 and no1 > 100 and no1 > 0)
print()
# or 연산자---------------------------------------------------------
# 1개 이상만 True가 되면 True 결정
print(no1 > no2 or no1 > 100)
print()
# not 연산자--------------------------------------------------
# 현재 값을 반대로 즉, True => False, False => True
# False => 0, True => 1/0이 아닌 모든 값
print(not False, not True)
print(not 0)
print(not 2)
print(not -3)
print(not 0.0)
'''

'''
객체 비교 연산자 => is, is not
- 결과 : True, False
- 동작방식
  * is => A is B  : A,B가 동일한 데이터 타입의 객체 여부
  * is not => A is not B : A,B가 서로 다른 데이터 타입의 객체 여부
'''

print(f'10 is 10 => {10 is 10}')
print(f'10 is 10.0 => {10 is 10.0}')
print(f'10 is 21 => {10 is 21}')


