#----------------------------------------------------
# 함수 안에 함수 정의 및 호출
#-----------------------------------------------------
'''
def print_hello():
    hello="hello~!"

    def print_message():
        msg=hello+"^^"
        print(hello)
    print_message()
    # print(msg) => 에러 발생

print_hello()
#print_message() -> 에러 발생

def a() :
    x=10
    def b():
        nonlocal x # 가장 가까운 바깥 함수에서 변수 x를 찾음
        x=20
    b()
    print(x)
a()

 '''
#----------------------------------------------------
# 함수 안에 함수 정의 및 호출
#-----------------------------------------------------

def foo() :
    x=10
    def test():
        return x
    return test

x=foo()
print(x(),x)











