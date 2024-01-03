#[실습]--------------------------------------------------
# -문자열 여러 개와 실수 여러 개를 입력받기 => input() 1개만 사용
# -첫번째 입력 받은 값은 Key
# -두번째 입력 받은 값은 Value
# -딕셔너리로 저장해주세요.
#-------------------------------------------------------

m_dict=dict()
data=input("문자열과 실수 여러개 입력 \n단, 문자열과 실수 갯수 동일(예:aa bb cc,1.1 2.2 3.3) : ")

#입력 형식이 맞을 경우엔 딕셔너리에 저장
# - (1) 입력 "," 문자열 안에 ',' 존재해야 함
# - (2) 문자열과 실수 갯수가 동일해야 함
if ',' in data :
    # dataList=data.split(',')
    # key=dataList[0].split(" ")
    # data=dataList[1].split(" ")
    key, data=data.split(',')
    key=key.split(' ')
    data=data.split(' ')
    if len(key)==len(data):
        # for i in range(len(key)):
        #     m_dict[key[i]]=data[i]
        #     #m_dict.setdefault(key[i], data[i])
        m_dict=dict(zip(key,data))
        print(m_dict)
    else :
        print("정확한 형식이 아닙니다.")
else :
    print("정확한 형식이 아닙니다.")




#-----------------------------------------
# 내장함수 zip()
#-----------------------------------------
x=[1,2,3,4,5]
y=[11,22,33,44,55]
z=[111,222,333,444,555]

print(zip(x,y,z))
print(list(zip(x,y,z))) # zip을 보기 위해서 list로 형변환
print(list(zip(x,zip(y,z))))
