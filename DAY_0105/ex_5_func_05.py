
# ----------------------------------------------------------------------
# 다양한 함수의 형태 - (5) 매개변수가 존재하지 않는 형태
# ----------------------------------------------------------------------

# 함수기능 : 인사 메시지 출력 가능
# 함수이름 : welcome
# 매개변수 : 없음
# 반환 값 : 츨력 결과

def welcome():
    print("ごんにちは")

welcome()

#함수기능 : 프로그램 정보 출력 기능
# 함수이름 : printInfo
# 매개변수 : 없음
# 반환 값 : str
def printInfo():
    return "MYNAME VERSION 1./\nDEVELOPER kk\nEWMAIL : master@game.com"

# 함수 사용 즉, 호출
welcome()
print(printInfo())