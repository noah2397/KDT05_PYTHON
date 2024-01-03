# 코딩도장 p.385 심사문제

def cal(x,y) :
    print(f"덧셈 : {x+y}, 뺄셈 : {x-y}, 곱셈 : {x*y}, 나눗셈 : {'나눗셈 오류' if not y else x/y}")


x, y=map(int, input().split())
cal(x,y)
