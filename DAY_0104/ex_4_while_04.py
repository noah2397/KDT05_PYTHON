#---------------------------------
# continue => 계속해서~
# -키워드 아래 코드 실행 안됨
# -반복 상단으로 이동
#---------------------------------
'''
# 1~30 으로 구성된 리스트 생성하세요, 짝수만 출력하세요
numList=list(range(1,31))
for data in numList :
    if not data%2:
        print(data)

for data in numList :
    if data%2 :
        continue
    print(data)


# Continue는 반복문의 맨 위로 이동하게끔 한다

# while ----------------------------------
numList=list(range(1,31))
idx=0
while idx < len(numList) :
    if not numList[idx]%2 :
        print(f'{idx}번째 요소 값 : {numList[idx]}')
    idx+=1
'''

numList=list(range(1,31))
idx=-1
while idx < len(numList)-1 :
    idx += 1
    if numList[idx]%2 :
        continue
    print(f'{idx}번째 요소 값 : {numList[idx]}')
