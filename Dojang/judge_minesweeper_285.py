# 코딩도장 p.285 심사문제
# 제 1안==================================================================================================================
if False :
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
# 112줄
"""
..*..
...*.
.*...
.***.
*.*..
"""
# 제 2안==================================================================================================================
if False :
    col, row = map(int, input().split())
    matrix=[]
    for _ in range(row) :   # 입력한 줄만큼 줄단위로 입력받음
          matrix.append(list(input()))
    matrix_full=[["." for i in range(col+2)] for j in range(row+2)] # 기존 col, row 2차원 배열보다 2씩 긴 큰 매트릭스 생성
    for i in range(row) :
        for j in range(col) :
            matrix_full[i+1][j+1]=matrix[i][j] # 큰 매트릭스에 값이 들어있는 매트릭스를 복사
    for i in range(1,row+1) :
        print_str=""  # 출력할 빈 str 생성
        for j in range(1,col+1) :
            count=0  # 3X3영역에 *개수를 세아릴 count변수 생성
            if matrix_full[i][j]=='.':
                for s in range(i-1, i+2) :
                    for k in range(j-1, j+2) :
                        if matrix_full[s][k]=="*" :  # s,k로 인덱스를 사용해서 *(별) 갯수 세아림
                            count+=1
                print_str+=str(count) # 다 세아리고 print_str에 갖다붙임
            else :  # 해당 영역이 그냥 *이라면 print_str에 *을 갖다붙임
                print_str+="*"
        print(print_str)
    # 22줄
# 3================================================================================================================================
if True : # chat gpt버전
    def count_adjacent_mines(matrix, row, col, i, j):
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < row and 0 <= nj < col and matrix[ni][nj] == '*':
                count += 1
        return count
    # 입력 받기
    row, col = map(int, input().split())
    matrix = []
    for i in range(row):
        matrix.append(list(input()))
    # 인접한 지뢰의 개수 계산
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '.':
                count = count_adjacent_mines(matrix, row, col, i, j)
                matrix[i][j] = str(count)
    # 결과 출력
    for i in range(row):
        print(''.join(matrix[i]))



