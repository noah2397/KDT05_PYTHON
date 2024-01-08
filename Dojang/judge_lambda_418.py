# 코딩도장 p.418 심사문제

#1.jpg 10.png 11.png 2.jpg 3.png
datas=input().split()
print(list(map(lambda x:f'{x[:x.find(".")]:0>3}{x[x.find("."):]}',datas)))