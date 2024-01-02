# 코딩도장 p.285 심사문제

# col, row = map(int, input().split())
# matrix=[]
# for _ in range(row) :
#         matrix.append(list(input()))
col, row= 5,5
matrix=[[".","*","*"],["*",".","."],[".","*","."]]
matrix=[[".",".","*",".","."],[".",".",".","*","."],[".","*",".",".","."],[".","*","*","*","."],["*",".","*",".","."]]
for i in range(col) :
    for j in range(row) :
        count=0
        if matrix[i][j]=="*" :
            print("*", end="")
            continue
        elif not i and not j :
            if matrix[i+1][j]=="*" :   # 아래
                count+=1
            if matrix[i][j+1]=="*" :   # 오른쪽
                count+=1
            if matrix[i+1][j+1]=="*":  #오른쪽 아래
                count+=1

        elif not i and j!=col-1 :
            if matrix[i+1][j]=="*" :   # 아래
                count+=1
            if matrix[i][j+1]=="*" :   # 오른쪽
                count+=1
            if matrix[i][j-1]=="*" :   # 왼쪽
                count+=1
            if matrix[i+1][j+1]=="*":  #오른쪽 아래
                count+=1
            if matrix[i+1][j-1]=="*":  #왼쪽 아래
                count+=1

        elif not i and j==col-1 :
            if matrix[i+1][j]=="*" :   # 아래
                count+=1
            if matrix[i][j-1]=="*" :   # 왼쪽
                count+=1
            if matrix[i+1][j-1]=="*":  #왼쪽 아래
                count+=1

        elif i!=row-1 and not j :
            if matrix[i-1][j]=="*" :   #위
                count+=1
            if matrix[i+1][j]=="*" :   # 아래
                count+=1
            if matrix[i][j+1]=="*" :   # 오른쪽
                count+=1
            if matrix[i-1][j+1]=="*":  #오른쪽 위
                count+=1
            if matrix[i+1][j+1]=="*":  #오른쪽 아래
                count+=1

        elif i!=row-1 and j==col-1 :
            if matrix[i-1][j]=="*" :   #위
                count+=1
            if matrix[i+1][j]=="*" :   # 아래
                count+=1
            if matrix[i][j-1]=="*" :   # 오른쪽
                count+=1
            if matrix[i-1][j-1]=="*":  #왼쪽 위
                count+=1
            if matrix[i+1][j-1]=="*":  #왼쪽 아래
                count+=1

        elif i==row-1 and not j :
            if matrix[i-1][j]=="*" :   # 위
                count+=1
            if matrix[i][j+1]=="*" :   # 오른쪽
                count+=1
            if matrix[i-1][j+1]=="*":  #오른쪽 위
                count+=1

        elif i==row-1 and j!=col-1 :
            if matrix[i-1][j]=="*" :   # 위
                count+=1
            if matrix[i][j-1]=="*" :   # 왼쪽
                count+=1
            if matrix[i][j+1]=="*" :   # 오른쪽
                count+=1
            if matrix[i-1][j+1]=="*":  #오른쪽 위
                count+=1
            if matrix[i-1][j-1]=="*":  #왼쪽 위
                count+=1

        elif i==row-1 and j==col-1 :
            if matrix[i-1][j]=="*" :   # 위
                count+=1
            if matrix[i][j-1]=="*" :   # 왼쪽
                count+=1
            if matrix[i-1][j-1]=="*":  #왼쪽 위
                count+=1

        elif i!=row-1 and j!=col-1:
            if matrix[i - 1][j] == "*":  # 위
                count += 1
            if matrix[i + 1][j] == "*":  # 아래
                count += 1
            if matrix[i][j + 1] == "*":  # 오른쪽
                count += 1
            if matrix[i][j - 1] == "*":  # 왼쪽
                count += 1
            if matrix[i-1][j+1]=="*":  #오른쪽 위
                count+=1
            if matrix[i-1][j-1]=="*":  #왼쪽 위
                count+=1
            if matrix[i+1][j+1]=="*":  #오른쪽 아래
                count+=1
            if matrix[i+1][j-1]=="*":  #왼쪽 아래
                count+=1
        print(count, end="")
    print()

