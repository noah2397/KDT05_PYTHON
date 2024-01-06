#32번

def getStarSign(month, day) :
    if month==1 :
        if day >= 20 :
            return "물병자리"
        else :
            return "염소자리"
    elif month==2 :
        if day >= 19 :
            return "물고기자리"
        else :
            return "물병자리"
    elif month==3 :
        if day>=21 :
            return "양자리"
        else :
            return "물고기자리"
    elif month==4 :
        if day>=21 :
            return "황소자리"
        else :
            return "양자리"
    elif month==5 :
        if day >= 21 :
            return "쌍둥이자리"
        else :
            return "황소자리"
    elif month==6 :
        if day >= 22 :
            return "게자리"
        else :
            return "쌍둥이자리"
    elif month==7 :
        if day >= 23 :
            return "사자자리"
        else:
            return "게자리"
    elif month==8 :
        if day >= 23 :
            return "처녀자리"
        else :
            return "사자자리"
    elif month==9 :
        if day >= 23 :
            return "천칭자리"
        else:
            return "처녀자리"
    elif month==10 :
        if day >= 22 :
            return "전갈자리"
        else:
            return "천칭자리"
    elif month==11 :
        if day >= 22 :
             return "사수자리"
        else:
            return "전갈자리"
    elif month==12 :
        if day >= 22 :
            return "염소자리"
        else:
            return "사수자리"
    else :
        "외계인이십니다"

animal=("원숭이","닭","개","돼지","쥐","소","호랑이","토끼","용","뱀","말","양")
jumin_num=input("주민번호 입력(000000-0000000) : ")

if jumin_num.find("-") != -1 :
    birth, code=jumin_num.split("-")
    if len(birth)==6 and len(code)==7 and int(code[0]) in (1,2,3,4): # 사람 맞는지 확인
        year=int("20"+birth[0:2]) if int(birth[0:2]) < 24 else int("19"+birth[0:2])
        month = int(birth[2:4])
        day = int(birth[4:6])
        print(f'{2024-year}세, {"남자" if int(code[0]) in (1,2) else "여자"}, {year}년 {month}월 {day}일 {animal[year%12]}띠 {getStarSign(month,day)}자리')


