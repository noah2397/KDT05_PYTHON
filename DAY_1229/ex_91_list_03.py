#---------------------------------------------------------------
# list의 원소/요소 데이터 변경 및 삭제
#---------------------------------------------------------------
# "Merry Christmas"의 문자 한개한개를 원소로 가지는 를 리스트로 생성하기
'''
chr_list=list("Merry Christmas")
print(chr_list)

# => " "데이터를 '***" 변경하기
print("\'" +chr_list[5]+"\'" )

chr_list[5]="***"
print(chr_list)  #str은 안되는데 list는 된다
# list는 요소 하나하나를 메모리 주소로 저장하기 때문에 주소만 바꿔주면 변경이 가능하다
# str은 덩어리째로 메모리 주소로 저장하기 때문에 주소를 바꾸면 전체값이 바뀌어야 해서 부분 수정이 불가능하다
'''



chr_list=list("Merry Christmas")
# 삭제 ==> del 데이터 또는 del(데이터) <- del은 명령어 취급한다
del chr_list[5]
print(f"chr_list => {chr_list}")  # *** 이 사라지고,
del chr_list[5]
print(f"chr_list => {chr_list}")  # 6번째 원소로 당겨진 "C"도 사라짐을 알 수 있다

del chr_list  #싹다 삭제





















