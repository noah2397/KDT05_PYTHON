#-------------------------------------------------------------------------
# [실습1] 2개의 정수를 입력받은 후 4칙 연산 수행 결과를 반환하는 기능의 함수 제작
#        함수이름 : fourCalc
#        매개변수 : a,b
#        반환결과 : 4칙 연산 결과
#-------------------------------------------------------------------------
def fourCalc(a,b):
    return a+b, a-b, a*b, ("나눗셈오류" if b==0 else a/b)
print(fourCalc(3,7))


#-------------------------------------------------------------------------
# [실습2] 문자열을 16진수 코드값으로 변환하는 함수 정의
#        함수이름 : getConde
#        매개변수 : msg
#        반환결과 : str
#-------------------------------------------------------------------------

def getConde(msg):
    result=""
    for data in msg :
        result+=hex(ord(data))+" "

    return result
print(getConde("asdfas"))


