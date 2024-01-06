#30번

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


jumin_num=input("주민번호 입력(000000-0000000) : ")
month=int(jumin_num[2:4])
day=int(jumin_num[4:6])
print(getStarSign(month,day))