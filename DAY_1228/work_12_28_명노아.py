#Q1

msg1='kim1234@naver.com'
print(msg1[:msg1.find("@")])
msg1='http://www.naver.com'
print(msg1[msg1.find("www")+len("www")+1:])
msg1='홍길동'
print(msg1[1:])
msg1='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(f"대문자만 출력 : {msg1[::2]}")
print(f"소문자만 출력 : {msg1[1::2]}")
msg1='ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(f"숫자만 출력 : {msg1[3::4]}")
msg1='881120-1068234'
print(f"생년월일 부분 : {msg1[:6]}, 숫자 부분 : {msg1[-7:]}")


#Q2
num1=int(input("정수 입력 : "))
print(f"10진수 : {num1}")
print(f"16진수 : {hex(num1)}")
print(f"2진수 : {bin(num1)}")
print(f"8진수 : {oct(num1)}")

#Q3
msg1=input()
msg2=input()
msg3=input()
print(f"코드 값이 가장 큰 단어 : {max(msg1,msg2,msg3)}")
print(f"코드 값이 가장 작은 단어 : {min(msg1,msg2,msg3)}")

#Q4
msg1="오늘은 과제와 함께하는 행복한 목요일이에요~😊"
keyword1=input("찾을 단어 입력 : ")
print(f"{keyword1} 단어 메시지 존재 여부 : {keyword1 in msg1}")



#Q5
msg1=input("단어 입력 : ")
print(f'\'{msg1}\' 코드값 : {bin(ord(msg1[0]))}  {bin(ord(msg1[1]))[2:]}  {bin(ord(msg1[2]))[2:]}')
