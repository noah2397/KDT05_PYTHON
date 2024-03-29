#-----------------------------------------------------
# List => 여러개의 데이터를 저장하는 데이터 타입
# - 문법 => [데이터1, 데이터2, ..., 데이터n ]
# - 원소/요소 => 식별하기 위해서 인덱스(Index) : 파이썬에 명명
# - 인덱싱 기능/슬라이싱 기능 모두 사용 가능
#------------------------------------------------------
'''
sevens=list(range(7,51,7))
print(sevens)

#str 데이터 타입 => 인덱싱 ----> 요소 변경 X
# 제일 첫번째 인덱스에 있는 원소 삭제
# ==> del 삭제하고 싶은 데이터 또는 del(삭제하고 싶은 데이터)
del sevens[0]
del(sevens[0])
print(sevens)

#del sevens #아예 sevens라는 리스트를 완전 삭제한다

# -------------------------------------------
# str 데이터 타입 => 인덱싱 ------> 요소 추가 X
# 리스트에 인덱싱 방식으로 원소/요소 데이터 변경 가능
#--------------------------------------------
# 요소 갯수 5개 => 0~4
# sevens[5]=56 # 다음 구문을 실행하면 에러를 표출한다(Index out of range)
sevens[4]=56  # 단순히 49있던 자리가 56으로 대체된다
print(sevens)
'''


