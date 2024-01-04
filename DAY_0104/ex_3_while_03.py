#-------------------------------------------------
# 반복문 - 2 while 반복문
# - 반복의 횟수 정해지지 않은 경우
#-------------------------------------------------
#[요청] 사용자가 'x'입력 전까지 입력받은 데이터 저장해주세요.
# => 몇 번 입력할지 알 수 없음 => 무한히 입력 받기
# -> 종료 조건 ==> 사용자 'x'입력
'''
while True :
    x=input("저장하고 싶은 데이터 입력 ( 종료 x ) :")
    # 종료 검사 => break : 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨
    if x in ['x','X']: break
    print("OK")
print("프로그램 종료")


#-----------------------------------------------
# [요청] 사용자로부터 x/X입력 전까지 계속 정수를 입력
#       입력받은 정수만큼 알파벳을 출력
# [예시] 출력 원하는 알파벳 수 입력 : 27
#       abcdefghijklmnopqrstuvwxyz 종료
# [예시] 출력 원하는 알파벳 수 입력 : 5
#       abcde
# [예시] 출력 원하는 알파벳 수 입력 : 6
#       abcdef
#------------------------------------------------


while True :
    alpha_str, num="", input("출력 원하는 알파벳 수 입력 : ")
    if num in ('x','X'):
        print("종료입니다")
        break
    for i in range(int(num)) :
        if i>=26 :
            alpha_str+=" 종료"
            break
        alpha_str+=str(chr(ord('a')+i))
    print(alpha_str)


while True :
    alpha_str, num="", input("출력 원하는 알파벳 수 입력 : ")
    if num in ('x','X'):
        break
    alpha_str=[chr(ord('a')+i) if i<=25 else " 종료" for i in range((int(num) if int(num)<=26 else 27)) ]
    print(('').join(alpha_str))
print("종료입니다")

while True :
    alpha_str, num="", input("출력 원하는 알파벳 수 입력 : ")
    if num.upper()=='X':
        break
    alpha_str=[chr(ord('a')+i) if i<=25 else " 종료" for i in range((int(num) if int(num)<=26 else 27)) ]
    print(('').join(alpha_str))
print("종료입니다")


isEnd=False #Flag 변수 선언
for n in range(100):
    print(f'out -> {n}')
    if isEnd:
        print("프로그램 종료합니다.")
        break
    for n2 in range(100):
        if n2>10:
            isEnd=True
            break
        print(f"in -> {n2} ====> {n}번째")
'''

n=0
while n <100:
    print(f'out -> {n}')

    for n2 in range(100):
        if n2>10:
            print("내부 while문 종료")
            n=100 # 전 플래그 변수 안썻어용
            break
        print(f"in -> {n2} ====> {n}번째")
    n+=1



