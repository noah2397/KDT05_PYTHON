#17번

def make_numset(msg) :
    numset=set()
    for i in msg :
        if i.isdecimal() :
            numset.add(i)
    for i, value in enumerate(numset):
        print(f'{value}', end=", " if i != len(numset)-1 else "")

msg=input("메시지 입력: ")
make_numset(msg)

#Happy New Year 2024!
#홍길동 010-1111-2222