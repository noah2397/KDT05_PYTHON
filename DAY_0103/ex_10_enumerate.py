#-----------------------------------------------
# for 요소 in 시퀸스/반복 가능한 객체
# ==> for 인덱스 in range(len(변수)) :
# ==> 내장함수 enumerate()
# - (번호, 데이터) 묶음으로 반환함!!!
#-----------------------------------------------
'''
datas=['Apple','Banana','Orange']

#리스트 안에 요소/원소 데이터 추출
for data in datas :
    print(data)
# 리스트 안에 요소/원소 (인덱스,데이터) 추출
for data in enumerate(datas) :
    print(data)

for data in enumerate(datas, start=100) :
    print(data)

'''
#언패킹 방식을 조합
myDict={}
x=['std01','std02','std03']
y=[100,200,300]
for idx, data in enumerate(x) :
    myDict[data]=y[idx]
print(myDict)




for key,value in myDict:
    print(key)