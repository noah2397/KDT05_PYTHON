#11번

bingo_num=99
while True :
    num=int(input("빙고 넘버 : "))
    if bingo_num > num :
        print(f"힌트 - {num}보다 큰 수")
    elif bingo_num < num :
        print(f"힌트 - {num}보다 작은 수")
    else :
        print("정답 - *~빙고 ~*")
        break




