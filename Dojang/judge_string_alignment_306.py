# 코딩도장 p.306 심사문제

# 입력 값 : 51900;83000;158000;367500;250000;59200;128500;1304000

price_list=list(map(int,"51900;83000;158000;367500;250000;59200;128500;1304000".split(";")))
print(price_list)
price_list.sort(reverse=True)

for data in price_list :
    print(f"{data:10,}")

