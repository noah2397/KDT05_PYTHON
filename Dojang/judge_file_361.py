# 코딩도장 p.361 심사문제
test="Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under paon of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report."

with open(r"C:\Users\mathn\Desktop\EXAM_PYTHON(23.12.26)\Python_Junior_institution\words.txt","r") as file :
    line=file.readline()
    print(line)
line_words=line.split()
for i in line_words :
    if 'c' in i :
        if i[-1] in ('.',',') :
            print(i[:-1])
        else :
            print(i)
