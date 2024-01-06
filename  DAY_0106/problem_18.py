#18번
#2024.01.08 기준 작성
#2000.04.01


def print_age(year,month,day) :
    print(f"당신의 한국 나이는 {2024 - year + 1}세 입니다.")
    if month > 1 or (month == 1 and day > 8):
        print(f"당신의 만 나이는 {2024 - year - 1}세 입니다.")
    else:
        print(f"당신의 만 나이는 {2024 - year}세 입니다.")


year, month, day=map(int,input("생년월일 입력 : ").split("."))

print_age(year,month,day)


