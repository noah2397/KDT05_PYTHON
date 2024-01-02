#---------------------------------------------------
# dict 데이터 전용 함수 즉 메서드(Method)
#---------------------------------------------------
# 빈 dict 타입 변수 생성-------------------------------
myDict={}


# 데이터 추가 => myDict[키]=데이터
myDict['one']=100

# 데이터 추가 => update(키=데이터) 메서드
# 주의!!! 키는 str 타입만 가능, str 타입이지만 '',"", 사용 안됨
#myDict.update('two', 200) <== EOFError
myDict.update(two=200, _1=1000)
print(myDict)

# 키만 추출해서 읽어오는 메서드 => keys() 메서드------------------------
keys=myDict.keys()
print(f"myDict의 키들 : {keys},   \t{type(keys)}")

# 값만 추출해서 읽어오는 메서드 => values() 메서드------------------------
values=myDict.values()
print(f"myDict의 값들 : {values}, \t \t{type(values)}")

# 키와 값을 묶어 추출해서 읽어오는 메서드 => items() 메서드------------------------
# (키, 값) 튜플 형식으로 묶어서
items=myDict.items()
print(f'myDict의 키/값 묶음들, {items}, \t{type(items)}')


# 원소/요소 단위 접근 위해서는 형변화 필요함!!
items=list(items)
print(items) # 리스트로 형변환을 해야 인덱스로 접근할 수 있다

# 원소/요소 모두 삭제해주는 메서드 => clear() 메서드 ==========================
# del myDict <- myDict를 없애면 안되므로 반복문을 써서 키값을 참조하여 삭제해야 한다
myDict.clear()
print(myDict)

#원소/요소 데이터 읽기 메서드 => 변수명[키] ===> 값, get(키) 메서드
# => 키가 존재하지 않으면 None 반환
#print(f'myDict.get("one") : {myDict.get("one")}, {myDict["one"]}')  # 키 에러로 인한 오류 발생
print(f'myDict.get("three") : {myDict.get("three")}')
#print(f'myDict["three"] : {myDict["three"]}')

#원소/요소 데이터 읽기 메서드 => 변수명[키] ===> 값, get(키) 메서드
# => 키가 존재하지 않으면 기본값 반환
print(f'myDict.get("one",0) : {myDict.get("one",0)}')
print(f'myDict.get("one","존재하지 않음") : {myDict.get("one","존재하지 않음")}')

#----------------------------------------------------
# 멤버 연산자 => 원소 in 여러개 저장 타입
#           => 원소 not in 여러개 저장  타입
# - 여러개 저장 타입 : str, list, tuple, dict, set
# - 연산 결과 => True/False
#----------------------------------------------------

aList=[1,2,3]
aTuple=11,22,
aDict={1:100, 2:200}

print(f"1 in aList : {1 in aList}")
print(f"1 in aTuple : {1 in aTuple}")
# 키 존재 여부 확인
print(f"1 in aDict : {1 in aDict}") # 이때는 값을 안보고 키만 본다
print(f"100 in aDict : {100 in aDict}") # 이때는 값을 안보고 키만 본다

