#4번
total_set=set()
for i in range(1,101) :
    if not i%3 or not i%7 or not i%8 :
        total_set.add(i)
print(total_set)