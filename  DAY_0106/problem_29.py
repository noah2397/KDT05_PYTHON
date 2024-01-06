#29번

members=dict()
def input_jumin(datas) :
    jumin=dict()
    for i in range(0,len(datas),3) :
        if i > len(datas) :
            break
        jumin[datas[i]] = datas[i + 2]
    members[f'{len(members)+1}']=jumin
    print(members)

while True :
    data=input("개인정보 : ").split()
    if data==['종료'] :
        break
    input_jumin(data)
# age – 12 id – mm1004   name - 마징가
# phone - 010-2222-1111 job - 히어로
# job - 학생 loc - 대구