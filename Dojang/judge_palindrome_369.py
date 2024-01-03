# 코딩도장 p.369 심사문제

with open(r"C:\Users\mathn\Desktop\EXAM_PYTHON(23.12.26)\Python_Junior_institution\words.txt","r") as file :
    line=file.readlines()
    for data in line :
        if data[:-1] == data[-2::-1] :
            print(data[:-1])