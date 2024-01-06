#21번

score_dict={"베트맨" : {"국어":90,"수학":89,"윤리":98,"국사":99},
            "마징가" : {"국어":82,"수학":71,"윤리":80,"국사":91},
            "슈퍼맨" : {"국어":77,"수학":100,"윤리":92,"국사":90},
            "슈렉" : {"국어":94,"수학":82,"윤리":93,"국사":71},
            "피오나" : {"국어":78,"수학":99,"윤리":91,"국사":83}}

for subject in ["국어","수학","윤리","국사"]:
    max, min = 0, 100
    for user in score_dict.keys():
        if score_dict[user][subject] > max :
            max = score_dict[user][subject]
        if score_dict[user][subject] < min :
            min = score_dict[user][subject]
    print(f"[{subject}] 최고 점수 : {max}, 최저 점수 : {min}")



