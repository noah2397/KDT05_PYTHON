# 실습1
# 알고싶은 단을 입력 받고 해당 단을 출력해주세요
#------------------------------------------

'''
num=input()
if num and num.isdecimal() :
    for i in range(1,10):
         print(f"{int(num): 1} * {i: 1} = {int(num)*i: 4}")
else :
    print("입력한 데이터가 없거나 잘못되었습니다")
'''


# for j in range(2,10) :
#     for i in range(1,10):
#          print(f"{j: 1} * {i: 1} = {j*i: 3}  ", end=" ")
#     print()


for j in range(0,10) :
    for i in range(2,10):
         print(f"   ---{i}단--- \t", end="" if i!=9 else '\n') if not j else print(f"{i: 1} * {j: 1} = {i*j: 3}", end="   " if i!=9 else '\n')