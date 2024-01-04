# 코딩도장 p.398 심사문제

#korean, english, mathematics, science = map(int, input().split())
korean, english, mathematics, science=76,82,89,84

def get_min_max_score(*args):
    return min(args), max(args)
def get_average(korean=0, english=0, mathematics=0, science=0):
    count,sum=0,korean+english+mathematics+science
    if korean > 0 :
        count+=1
    if english > 0 :
        count+=1
    if mathematics > 0 :
        count+=1
    if science > 0 :
        count+=1
    return sum/count

min_score, max_score= get_min_max_score(korean, english, mathematics, science)
average_score=get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수:{average_score:.2f}')
min_score, max_score=get_min_max_score(english, science)
average_score=get_average(english=english, science=science)
print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수:{average_score:.2f}')