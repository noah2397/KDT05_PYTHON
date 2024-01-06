#14 번
# 1234567, $
# 907, W
data=input("숫자 입력 : ")
price, unit = int(data[:data.index(",")]), data[data.find(",")+2]
print(f"{price:,}{unit}")