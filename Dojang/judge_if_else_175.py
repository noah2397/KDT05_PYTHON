# 코딩도장 p.175 심사문제


score=list(map(int,input().split()))
if all(s <= 100 for s in score) :
    if sum(score)/4 >= 80 :
        print("합격")
    else :
        print("불합격")
else :
    print("잘못된 점수")

# 89 72 93 82  합격
# 100 79 68 71 불합격
# 99 85 101 90 잘못된 점수