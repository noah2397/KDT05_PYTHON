#-------------------------------
# #나의 프로그램 : 계산기
# [ 계산기 ]
# 1. 데이터 입력
# 2. 덧셈
# 3. 뺄셈
# 4. 곱셈
# 5. 나눗셈
# 6. 기록보기
# 7. 검색
# 8. 삭제
# 9. 종료
#--------------------------------
# 사용자 정의 함수 -----------------
# 함수 기능 : 연산결과 리스트에서 검색어에 해당하는 데이터만 출력
# 함수 이름 : searchResult
# 매개 변수 : search
# 함수 결과 : None(없음)
#---------------------------------

def searchResult(search):
    searchList, count=[], 0
    for i in calcList :
        if search in i :
            searchList.append(i)
            count+=1

    print(f"총 {count}건의 검색 결과가 있습니다 : \n") if count else print("검색결과 없다!")
    for i in searchList :
        print(i)
    print()


# 계산 기록 저장할 전역변수 선언
calcList=[]

while True:
    print("1. 입 력\n"
          "2. 덧 셈\n"
          "3. 뺄 셈\n"
          "4. 곱 셈\n"
          "5. 나눗셈\n"
          "6. 기록보기\n"
          "7. 검 색\n"
          "8. 삭 제\n"
          "9. 종 료\n")
    choice = input("메뉴 선택 : ")
    if choice.isdecimal() :
        if choice=="1":
            data=input("2개 정수 (예 : 10 20) : ")
            n1,n2=list(map(int,data.split()))
        elif choice=="2":
            calcList.append(f'덧셈결과 : {n1} + {n2} = {n1 + n2}')
            print(calcList[-1])
        elif choice=="3":
            calcList.append(f'나눗셈결과 : {n1} - {n2} = {n1 - n2}')
            print(calcList[-1])
        elif choice=="4":
            calcList.append(f'곱셈결과 : {n1} * {n2} = {n1 * n2}')
            print(calcList[-1])
        elif choice=="5":
            calcList.append(f'나눗셈 결과 : {n1} % {n2} = {("오류" if not n2 else n1/n2)}')
            print(calcList[-1])
        elif choice=="6":
            for i in range((5 if len(calcList)>5 else len(calcList))):
                print(f'{i+1}번 최근항목 : {sorted(calcList,reverse=True)[i]}')
        elif choice=="7":
            searchResult(input("검색할 단어를 입력해주세요 : "))
        elif choice=="8":
            ok=input("정말 지우겠습니까? n/y :")
            if ok=='y':
                calcList.clear()
                print("모든 계산기록이 날아가부렀으께~")
        elif choice=="9":
            print("프로그램 종료합니다.")
            break
        else :
            print("메뉴 1~9까지 선택 가능합니다.")
    else :
        print("잘못 입력하셨는데요???")