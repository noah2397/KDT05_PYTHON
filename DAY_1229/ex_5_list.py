#---------------------------------------------------
# 리스트(List) 데이터 타입
# -여러 종류의 여러 개의 데이터를 저장하는 타입
# -문법 : [ 데이터1, 데이터2, ...., 데이터 N ]
# -특징 : 데이터 하나 하나를 요소/원소라고 함
#        하나하나의 요소/원소를 식별하기 위해서 인덱싱(Indexing)
# -순서가 있는 데이터 타입 => 시퀸스 데이터 타입
#---------------------------------------------------
'''
#리스트 데이터 생성-----------------------------
# 숫자 10개를 메모리에 저장
no1=10
no2=30
no3=100
no4=5
no5=104
no6=-1205
no7=105
no8=104
no9=103
no10=-101
#    0  1  2  3  4  5  6  7  8  9
no=[10,20,30,40,50,60,70,80,90,100]
print(f"id(no) => {id(no)}\nid(no[0]) => {id(no[0])}")
'''

# 리스트의 원소/요소 한 개씩 접근하는 방법 => 변수명[인덱스]--------
# - 왼쪽 => 오른쪽 : 0~
# - 오른쪽 => 왼쪽 : -1~
# => 슬라이싱 가능
#----------------------------------------------------------
# 마지막 3개의 정수만 출력해주세요

no=[10,20,30,40,50,60,70,80,90,100]
print(no[-3:])

#짝수번째 인덱스 요소만 출력해주세요
print(f"짝수 요소만 출력 : {no[::2]}")
print(f"홀수 요소만 출력 : {no[1::2]}")













