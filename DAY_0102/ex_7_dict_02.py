#------------------------------------------
# 다양한 dict자료형 => key:value <= 데이터 덩어리
# -key로 데이터를 찾기/읽기/삭제/변경
# -key 중복 X => 마지막 데이터의 key의 값으로 저장
#-----------------------------------------
#이름, 점수 저장하기
jumsuDict={"Hong":100,"Park":98,"Kim":88,"Hong":50,"Hong":77}
print(f'딕셔너리 길이 및 요소 : {len(jumsuDict)}, {jumsuDict}')
# 똑같은 키가 들어오면 제일 마지막에 들어오는 값이 저장된다


# 이름/학년을 키로 해서 점수를 저장하기 ------------------------------
jumsuDict={('Hong',1):100,('Park',3):98,('Kim',1):88,('Hong',4):50,('Hong',2):77,}
print(f'딕셔너리 길이 및 요소 : {len(jumsuDict)}, {jumsuDict}')
print(f'jumsuDict[("Hong",2)] :{jumsuDict[("Hong",2)]}')
print(f'jumsuDict[("Hong",1)] :{jumsuDict[("Hong",1)]}')


# 키의 데이터 타입 동일해야 하나요?? 아닙니다,
testDict={1:'hong',2.0:'KIM',False:100,"name":"HongilDong", False:2024}
print
print(f'딕셔너리 길이 및 요소 : {len(jumsuDict)}, {jumsuDict}')