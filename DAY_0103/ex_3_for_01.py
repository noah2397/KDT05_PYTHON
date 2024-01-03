# 1~100 사이의 2의 배수에 해당한 정수로 리스트 생성
two=list(range(2,101,2))
print(two)

# "24681012...100" 만들기
#result=str(two)
#print(result)

strNum=''
# 시퀸스 데이터 타입에서 원소/요소를 하나씩 빼서 반복 코드 수행
for num in two :
    strNum+=str(num)
print(strNum)