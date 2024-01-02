#--------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드(Method)살펴 보기
# -메서드(Method)
#  특정 데이터 타입에서만 사용 가능한 함수를 의미
# -사용방법
#  변수명, 메서드명() ==> msg="Good"
#                      msg.메서드명()
#  데이터.메서드명()  ==> "Good".메서드명()
#--------------------------------------------------
'''
print("Good".upper())  #원본은 안바꾸고 복사본을 주는 메서드이다, 대문자로 바꿔주는 메서드
print("Good".lower())  # 소문자로 바꿔주는 메서드
'''

'''
# str이 모두 대문자인지 검사 후 결과 반환 => isupper()
print("Good".isupper()) # 소문자 o가 있기 때문에 False출력된다
# str이 모두 소문자인지 검사 후 결과 반환 => isupper()
print("Good".islower())
# str이 모두 0~9로 구성되어 있는지 검사 후 결과 반환 => isupper()
print("Good".isdecimal(), "012".isdecimal(), "-9".isdecimal(), "\n") #-는 기호라서 False가 뜬다!

#str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print("Good".isalpha(), "Good2024".isalpha(), "한글".isalpha(), "\n") #2024가 있기 때문에 False가 나온다

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum() 메서드
print("Good".isalnum(), "Good2024".isalnum(), "한글".isalnum(), "\n")

# str 문자에서 특정 문자/문자열로 시작하는지 검사 후 결과 반환
# 시작 => ??
print("??Happy New".startswith("??"))
print("??Happy New".startswith("Ha"), "\n")

# str 문자에서 특정 문자/문자열로 끝나는지 검사 후 결과 반환
# 끝 => .jpg
print("flower.jpg".endswith(".jpg"))
print("flower.png".endswith(".jpg"), "\n")
'''

'''
# 튜플을 사용한 endswith 메서드 사용방법
print("flower.png".endswith((".jpg",".png")), "\n")

# str 특징 인덱스 문자를 변경해주는 메서드 => replace()메서드 ---------
name="HongGulDong"
#     01234567890
# => u ===> i 로 변경
print(name[5])
#name[5]='i'  #에러가 뜬다, 스트링은 할당 기능을 지원하지 않는다
name=name.replace('u','i') # 네 번째 인자 Count는 기본값 -1로 들어가있다
print(name) # 저장을 하고 치환되어 잘 출력된 모습
name=name.replace('o','*', 1) # 하나만 바꾼다는 뜻이다
print(name) # 저장을 하고 치환되어 잘 출력된 모습 # o가 *로 하나만 바꼈음을 알 수 있다
'''










