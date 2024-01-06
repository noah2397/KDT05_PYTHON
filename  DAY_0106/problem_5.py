#5번
data="가나다"

data_in_bi=""
data_in_hex=""
for i in data :
    data_in_bi+=str(bin(ord(i)))
    data_in_hex+=str(hex(ord(i)))
print(f'"가나다"의 인코딩 : {data_in_hex}')
print(f'"가나다"의 인코딩 : {data_in_bi}')
