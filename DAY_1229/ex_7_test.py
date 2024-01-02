#-----------------------------------------
# [실습1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#         리스트에 원소를 하나씩 화면에 출력하세요
#-----------------------------------------
num_list=[1,2,3,4,5,6,7]
print(num_list[0], end=" ")
print(num_list[1], end=" ")
print(num_list[2], end=" ")
print(num_list[3], end=" ")
print(num_list[4], end=" ")
print(num_list[5], end=" ")
print(num_list[6])
#아래 리스트에서 원소를 화면에 한 줄로 한개씩 표현하세요
datas=[[10,20],[40,50],[70,80,90]]
print(datas[0][0], end=" ")
print(datas[0][1], end=" ")
print(datas[1][0], end=" ")
print(datas[1][1], end=" ")
print(datas[2][0], end=" ")
print(datas[2][1], end=" ")
print(datas[2][2])

for i in datas:
    for j in i:
        print(j, end=" ")

#좋아하는 계절과 월을 입력받은 후 각각 변수에 저장하세요
#변수명은 season, month입니다.
#season, month =input("좋아하는 계절과 월을 입력하세요").split()
#1~20으로 구성된 점수 리스트를 생성하세요
# 그리고 3의 배수 인덱스에 해당하는 정수만 출력하세요
num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print(num_list[3::3])
#print(sum(num_list[3::3]))


print(num_list[:1]) # 이러면 정수가 아니라 슬라이싱이끼 때문에 리스트 형태로 나온다