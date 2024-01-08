# ---------------------------------------------------------
# 전역변수 (Global Variable)


# 사용자 정의 함수 -----------------------------------
def currentDate(todays):
    #todats => 년, 월, 일을 원소로 담고 있는 데이터 타입, 리스트
    todays[0]=todays[0]+10
    print(f"Today : {todays[0]}/{todays[1]:0>2}/{todays[2]:0>2}")

# 전역 변수 --------------------------------------
year,month,day=2024,1,8
todayList=[year,month,day]


print(f'year : {year}, month : {month}, day : {day}')
print(todayList)
currentDate(todayList)
print(f'year : {year}, month : {month}, day : {day}')
print(todayList)




