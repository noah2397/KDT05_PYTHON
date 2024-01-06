#7번 문제

nums = [0,1,2,4,5,2,9,3,2,8,1]
#nums = [0, 1, 2, 4, 5, 2, 9]
#nums = [ 0, 1, 2, 4, 5, 3, 1, 7 ]
#nums = [ 0, 0, 0 ]

idx_2=nums.count(2)
if idx_2 == 0 :
    print("[-1]")
elif idx_2 == 1 :
    print("[2]")
else :
    save=[]
    for i in range(nums.index(2),len(nums)-nums[::-1].index(2)) :
        save.append(nums[i])
    print(save)

