#15번

season_dict={1:"일",2:"이",3:"삼",4:"사",5:"오",6:"육",7:"칠",8:"팔",9:"구",10:"십",11:"십일",12:"십이"}
season_dict2={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"Novemver",12:"December"}

season_input = int(input("좋아하는 월 : "))
print(f"{season_dict2[season_input]} {season_dict[season_input]}월")