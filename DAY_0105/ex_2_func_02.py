# ----------------------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# ----------------------------------------------------------------------
# 함수기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
# 함수이름 : fact
# 매개변수 : n
# 반환 값 : fact(n-1) * n
# ----------------------------------------------------------------------

def fact(n) :
    if not n:
        return 1
    return fact(n-1)*n



print(fact(5))

#----------------------------------------------------------------
# 함수 기능 : 팩토리얼 계산 후 계산 결과를 아래와 같은 형태로 반환해주는 기능
#           예시 결과 : 3! = 3 * 2 * 1
# 함수 이름 : factorial2
# 매개 변수 : x
# 반 환 값 : 계산 str
#----------------------------------------------------------------

def factorial2(n) :
    print_str,result="",1
    print_str+=(str(n)+"! =")
    for i in range(n,0,-1) :
        result*=i
        print_str+=((" "+str(i)+" *") if i!=1 else ((" "+str(i)+" =")))
    return print_str+(" "+str(result))


'''
def factorial2(n) :
    strRet=f'{n}! = '
    intRet=1
    for n in range(n,0,-1) :
        strRet=strRet+str(n)
        strRet = strRet + (' * ' if n!= 1 else ' = ')
        intRet=intRet * n
    strRet = strRet + str(intRet)
    return strRet
'''
print(factorial2(0))
