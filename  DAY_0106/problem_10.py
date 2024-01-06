#10번
# '123,42,98,18'
# '1,234'

data=input("data=")
data_after=list(map(int, data[data.index("'")+1:len(data)-data[::-1].index("'")-1].split(",")))
print(f"\"{data[1:-1]}\"의 합 : {sum(data_after)}, 가장 큰 수 : {max(data_after)}, 가장 작은 수 : {min(data_after)}")
