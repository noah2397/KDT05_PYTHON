#19번


num=int(input("팩토리얼 수 입력 : "))
fac=1
msg=f'{num}! => '
while num :
    msg+=f'{num} * ' if num!=1 else f'{num} = '
    fac*=num
    num-=1

print(msg+f'{fac}')
