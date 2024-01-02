# 임의의 숫자(정수)를 저장 후, 짝수면 짝수입니다, 홀수면 홀수입니다라고 출력

'''ㅌ
myNum=-71

# 숫자 % 2 == 0 : 짝수, 숫자 % 2 == 1 : 홀수
if myNum % 2 == 0 :
    print(f"{myNum} 짝수입니다.")
else :
    print(f"{myNum} 홀수입니다.")

print("홀수입니다") if int(input("좋아하는 정수 입력 : "))%2 else print("짝수입니다")



# 좋아하는 정수를 하나 저장한 후 양수면 "  "은 양수입니다
# 음수면 "  "은 음수입니다 출력
# 다중 조건문 (if가 2개 이상일 때)
myNum=-71
if myNum > 0 :
    print(f"{myNum}은 양수")
elif myNum < 0 :
    print(f"{myNum}은 음수")
else :
    print(f"{myNum}은 0")

print(f"{myNum}은 양수") if myNum>0 else print(f"{myNum}은 음수")
'''
myNum=-71
if myNum > 0 :
    print(f"{myNum}은 양수")
    if myNum < 0 :
        print(f"{myNum}은 음수")
    else :
        print(f"{myNum}은 0")
