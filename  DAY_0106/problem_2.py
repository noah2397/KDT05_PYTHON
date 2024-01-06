#2번
#"하늘 Apple 2021 –9 False 23 7 None 끝"
#"A 홍길동 False True True None Good Luck 가나다라"
input_value=input("데이터 입력 : ")
save_list=[]
for i in input_value.split(" ") :
    if i.isnumeric() or (i[0] == '-' and i[1:].isnumeric()):
        save_list.append(int(i))
print(f"합계 : {0 if not save_list else sum(save_list)}, 최댓값 : {0 if not save_list else max(save_list)}, 최솟값 : {0 if not save_list else min(save_list)}")


