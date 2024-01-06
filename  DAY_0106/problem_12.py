#12번

num=int(input("게임 정수 입력 : "))
for i in range(1, num+1) :
    print(f'{"#" if i%10 in (2,4,8) else i}', end="" if i%20 else "\n")
