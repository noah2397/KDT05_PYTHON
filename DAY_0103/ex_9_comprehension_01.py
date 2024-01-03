#------------------------------------------------------------
# 컨프리헨션(Comprehension)
# -List Comprehension, Dict Comprehension, Set Comprehension
#------------------------------------------------------------

# [실습] aList의 원소 값을 제곱한 값을 원소로 가지는 bList 생성하세요
aList=[1,2,3,4]
bList=[i**2 for i in aList]
print(bList)


# [실습] aList의 원소 값 중에서 짝수인 데이터만 제곱한 값을 원소로 가지는 bList 생성하시오

# 컨프리헨션 방식-----------------------------------------
bList=[i**2 for i in aList if not i%2]
#      (1)        (2)           (3)
# 3번 조건을 만족시키는 값에 한해서 2라는 for문 요소들에서 1을 활성화
print(bList)


# [실습] aList의 원소 값 중에서 짝수인 데이터는 제곱, 홀수인 데이터는 그대로 하는 값을 가지는 bList 생성하시오
bList=[i**2  if not i%2 else i for i in aList]
print(bList)

cList={i:i**2  if not i%2 else i for i in aList}
print(cList)

