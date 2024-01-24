# 코딩도장 p.447 심사문제

class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    @staticmethod
    def is_time_valid(str):
        hour, minute, second=map(int, str.split(":"))
        if (hour <= 23 and hour >=0) and (minute <=59 and minute >=0) and (second <=59 and second>=0) :
            return True
        else :
            return False
    @classmethod
    def from_string(cls, str=""):
        hour, minute, second=map(int, str.split(":"))
        t=cls(hour, minute, second)
        return t

time_string=input()


if Time.is_time_valid(time_string):
    t=Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else :
    print("잘못된 시간 형식입니다")

# 23:35:59
# 12:62:43