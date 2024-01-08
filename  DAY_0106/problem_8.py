#8번 문제

#nums=[-2,3,0,2,-5]
nums=[-3, -2, -1, 0, 1, 2, 3 ]
nums_set=set(nums)
nums_set_save=[]
count_num=0
for i in range(2**len(nums)) :
    subset= set()
    for j in range(len(nums)):
        if (i >> j) & 1 :
            subset.add(nums[j])
    if not sum(list(subset)) and len(subset) == 3 and subset not in nums_set_save :
        count_num+=1
    nums_set_save.append(subset)
print(count_num)