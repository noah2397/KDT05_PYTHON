#9번

n=int(input("단 : "))
print(f"{'-'*20}{n}단{'-'*20} ")
for i in range(3) :
    for j in range(1,4) :
        print(f'{n:2} * {i*j:2} = {n*i*j:2}\t', end="" if j!=3 else "\n")