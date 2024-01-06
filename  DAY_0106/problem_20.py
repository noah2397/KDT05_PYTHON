#20번

#에라토스테네스의 체를 사용하여 소수 판별
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    # 에라토스테네스의 체를 사용하여 소수 판별
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_prime2(n) :
    flag=0
    if n==1 :
        return False
    for i in range(2,n+1) :
        if not n%i:
            flag+=1
        if flag and i<n :
            return False
    return True


num=int(input("범위 숫자 입력 : "))
print(f"1 ~ {num} 범위에서 소수 : ", end="")
prime=[]
for i in range(1,num+1):
    if is_prime2(i) :
        prime.append(i)
for i in range(len(prime)):
    print(f"{prime[i]}", end=", " if i != len(prime)-1 else "")