#28번

def cal(n1,n2):
    return n1+n2,n1-n2,n1*n2,0 if not n2 else n1/n2,0 if not n2 else n1//n2,0 if not n2 else n1%n2

n1,n2=map(int, input("숫자 2개 입력 (3,4) : ").split(", "))
plus,minus,multi,div,quotient, remainder=cal(n1,n2)
print(f"덧셈 결과 : {plus}")
print(f"뺄셈 결과 : {minus}")
print(f"곱셈 결과 : {multi}")
print(f"나눗셈 결과 : {div}")
print(f"몫 결과 : {quotient}")
print(f"나머지 결과 : {remainder}")
