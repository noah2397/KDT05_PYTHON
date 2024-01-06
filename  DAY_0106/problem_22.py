#22번


start, end =map(int,input("시작 구구단, 종료 구구단 입력 : ").split(" - "))
start_con, end_con =start, end
flag_print_title=1
flag_print_cal=1
while True :
    if flag_print_title :
        print(f"--[{start}]--  ", end="" if start!=end else "\n")
        start+=1
    if start==end+1 and flag_print_title:
        flag_print_title, start=0, start_con

    if not flag_print_title and flag_print_cal <= 9 :
        print(f'{start}*{flag_print_cal}= {start*flag_print_cal:<3} ', end="" if start!=end else "\n")
        start+=1
        if start==end+1 :
            start=start_con
            flag_print_cal+=1
    if flag_print_cal == 10:
        break





