#24번


def print_num(n):
    print(f"숫자 : {n}")
    unit_dict={"일":None,"십":None,"백":None,"천":None,"만":None,"십만":None,"백만":None,"천만":None,"헉":None}
    for idx, key in enumerate(unit_dict.keys()) :
        unit_dict[key]=n%10
        n=int(n/10)
        if not n:
            break
    key_result=list(unit_dict.keys())
    value_result=list(unit_dict.values())
    #print(key_result, value_result )
    for i in range(len(value_result)-1,-1,-1):
        if value_result[i]==None :
            continue
        print(f'{key_result[i]}의 자리 : {value_result[i]}')


num=int(input("숫자 입력 : "))
print_num(num)