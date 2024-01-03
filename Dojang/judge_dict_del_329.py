# 코딩도장 p.329 심사문제

#alpha bravo charlie delta
#10 20 30 40
#alpha bravo charlie delta echo foxtrot golf
#30 40 50 60 70 80 90

keys=input().split()
values=map(int,input().split())
x=dict(zip(keys, values))
x={i:j for i,j in x.items() if i!="delta" and j!=30}
print(x)