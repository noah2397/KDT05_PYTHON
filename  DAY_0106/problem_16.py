#16번

num1,num2= map(int, input("약수 구하고 싶은 수 : ").split())
save =[]
print(f"{num1}, {num2}의 공약수 : ")
for i in range(1,max(num1,num2)+1) :
    if not num1%i and not num2%i :
        save.append(i)
for i in range(len(save)) :
    print(f'{save[i]}', end=", " if i != len(save)-1 else "")