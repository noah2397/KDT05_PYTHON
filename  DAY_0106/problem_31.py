#31번

while True :
    year=int(input("년도 입력 :"))
    print(f"{year}년은 윤년입니다") if not year%400 or (not year%4 and year%100) else print(f"{year}년은 평년입니다")



