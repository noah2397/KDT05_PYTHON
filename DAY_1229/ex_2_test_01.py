# 단어를 입력받고 입력받은 단어가 알파벳만으로 구성되어있는지 검사
# 숫자만으로 구성되어 있는지 검사
# 모두 대문자로 구성되어있는지


str1=input("메시지를 입력하세요 : ")
print(f"{str1.isalpha(), str1.isdecimal(), str1.isupper(), str1.islower()} ")





# 파일명을 입력받은 후 아래 코드를 작성
# 입력받은 파일이 text파일인지 검사
# 입력받은 파일이 jpg 파일인지 검사
# 입력받은 파일이 py 파일인지 검사

file_name=input("파일명을 입력하세요 : ")
print(f"{file_name.endswith('.txt')}")
print(f"{file_name.endswith('.jpg')}")
print(f"{file_name.endswith('.py')}")