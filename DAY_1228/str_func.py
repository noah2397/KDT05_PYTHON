#--------------------------------------------------------------
# str 데이터 타입과 관련된 내장 함수
#--------------------------------------------------------------

# 원소/요소의 갯수를 알려주는 내장함수 => length의 약자 len()
msg="christmas2023!"

print(f'len(msg) => {len(msg)}개')
#print(f'len(2024) => {len(2024)}개') #정수는 길이를 가지고 있지 않아서 오류가 난다



# 인코딩 : 사람의 언어를 컴퓨터의 언어로 바꾸는 과정
# 문자의 코드값을 알려주는 매칭 함수 => ord(문자 1개)

print(f"ord('a') => {ord('a')}") #두개는 못넣는다

# Hello의 코드값 출력하기
codeH=ord('H')
codee=ord('e')
codel=ord('l')
codeo=ord('o')
print(f"Hello 의 코드값 => {codeH,codee,codel,codel,codeo}")
print(f"Hello 의 이진코드값 => {bin(codeH)[2:],bin(codee)[2:],bin(codel)[2:],bin(codel)[2:],bin(codeo)[2:]}")



# 코드값을 문자로 바꿔주는 함수 => chr(숫자1개)
print(f'chr(65) => {chr(65)}')













