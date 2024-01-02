#---------------------------------------------------
# str 데이터에서 문자열 분리해주는 메서드 => split() 메서드
# -기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러개의 str 분리
#----------------------------------------------------

data="Happy New Year"
datas=data.split()
print(type(datas), datas)

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print(f"datas[0] => {datas[0]}")
print(f"datas[0] => {datas[1]}")
print(f"datas[0] => {datas[2]}")
print(f"datas[0] => {datas[-1]}")

juminNo="123456-1234567"
#        01234567890123
birth = juminNo[:6]
number = juminNo[7:]



print(birth, number)
juminNos=juminNo.split("-")
print(juminNos)

# 하이픈("-")인덱스를 찾아 분리하는 방법도 있다.

birth=juminNo[:juminNo.index('-')]
number=juminNo[juminNo.index('-')+1:]
print(birth, number)
