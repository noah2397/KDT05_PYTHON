#13번
# 썅 잘못 만듦 ㅋㅋㅋㅋㅋ
# season=("january","february","march","april","may","june","july","august","september","octeober","november","december")
# season_input=input("좋아하는 월 입력 : ")
#
# if season_input.lower() in ("january","february","december") :
#     print(f"{season_input} Winter")
# elif season_input.lower() in ("march","april","may") :
#     print(f"{season_input} Spring")
# elif season_input.lower() in ("june","july","august") :
#     print(f"{season_input} Summer")
# elif season_input.lower() in ("september","octeober","november") :
#     print(f"{season_input} Fall")

season_input=int(input("좋아하는 월 입력 : "))
if season_input in (12,1,2) :
    print(f"{season_input} Winter")
elif season_input in (3,4,5) :
    print(f"{season_input} Spring")
elif season_input in (6,7,8) :
    print(f"{season_input} Summer")
elif season_input in (9,10,11) :
    print(f"{season_input} Fall")
else :
    print("존재하지 않는 월입니다")