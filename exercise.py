def function(a) :
    ''' 독스트링 : 함수에 대한 설명을 넣을 수 있습니다'''
def function2(a) :
    '''
        여러 줄로 된 설명도 가능
        근데 이거 그냥 주석 기능 아니냐...?
        독스트링 윗줄에 다른 코드가 오면 안된다
    '''
#  코드 작성 부분

print(function.__doc__)
print(function2.__doc__)
# __doc__으로 독스트링을 출력할 수 있다