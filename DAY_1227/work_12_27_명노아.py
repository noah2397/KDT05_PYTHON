#Q1.

fusujato="대구"
ketsueki="A"
kisetsu="Winter"
height=184
denwabanggo="010-4822-4335"
nation="한국"

#Q2.
mbti='ISFJ'
blood='A'
gender='M'
height=184.0
weight=76

print("[신상정보]")
print("MBTI : ", mbti, "혈액형 : ", blood, "성별 : ", gender,"\n","몸무게 : ", weight, "키 : ", height)
print("MBTI :  %s   혈액형 :  %s, 성별 :  %s\n몸무게 :  %d 키 : %f "%(mbti, blood, gender, height, weight))
print(f"MBTI : {mbti}    혈액형 : {blood}     성별 : {gender}\n"
      f"몸무게 : {weight}     키 : {height} ")

#Q3.
print(f"데이터 50 => {type(50)}타입")
print(f"데이터 0.91 => {type(0.91)}타입")
print(f"데이터 Winter => {type('Winter')}타입")
print(f"데이터 False => {type(False)}타입")

#Q4.
#위에서부터 힙, 스택



#Q5.
#int, float, str, bool
#2진수, 8진수, 16진수

#Q6.
garo=int(input("직육면체 가로길이(cm) : "))
sero=int(input("직육면체 세로길이(cm) : "))
height=int(input("직육면체 높이길이(cm) : "))
print(f"직사각형 넓이 : {garo*sero}\n"
      f"직사각형 부피 : {garo*sero*height}")
