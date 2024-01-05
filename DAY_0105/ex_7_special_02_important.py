#---------------------------------------------
# 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# 키와 값의 덩어리 데이터
# 형태 : def 함수명(**data):
# 가변 인자 함수
# 매개변수 갯수 : 0개~N개
# 호출 : 함수명(키1=값1)
#       함수명(키1=값1, 키2=값2, 키3=값3)
#       함수명()
#---------------------------------------------
'''
aDict={'name':'Hong','age':10}
aDict.update(job="학생", birth="1112", blood='A')
print(aDict)


#------------------------------------------------------------
# 함수 기능 : 회원 가입 가능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ......
#            가변 + 데이터 정보 함께
#            키워드 파라미터 **member
# 반 환 값 : '가입 완료 되었습니다.'str
#------------------------------------------------------------
def joinMember(**member) : # 키=값, 키=값 ....

    #멤버 저장소에 멤버 추가하기
    members.append(member)  #방법 1.  members가 리스트일 때, 키=값, 키=값 이렇게 만들어준다
    for k,v in member.items() :  # 방법 2.members가 딕셔너리일 때, 이렇게 따로따로 넣으면 키=값 단위로 한번에 다 처박히게 된다
        members[k]=v
    members[f'MP{len(members)}']=member # 방법 3. members가 딕셔너리일 때, 값을 딕셔너리로 넣을 수 있다
    print(members)

#-----------------------------
# 함수 사용 즉 호출
#-----------------------------
# 가입된 회원들 저장 변수
members={}
#members.keys()
#members.values()
#members.items()

example={"name":"Hong", "age":17}
# 회원가입 기능 함수 호출
joinMember(name='Hong', age=17, birth='20201010')
joinMember(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
joinMember(**example) # 해당 함수에 딕셔너리 타입을 넣을 때, **을 붙여서 넣어야 한다
#joinMember(id='Hong84', birth='2024/01/01', blood='A')





#------------------------------------------------------------
# 함수 기능 : 회원 가입 가능
# 함수 이름 : joinMember2
# 매개 변수 : 필수 => id, pw
#            선택 => **option => 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ......
#            가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.'str
#------------------------------------------------------------
def joinMember2(id,pw,**option) :
    # 멤버 저장소에 멤버 추가하기
    members[f'len(members)+1']=[id, pw, option]
    print(members)

members={}

joinMember2('h','ph')
joinMember2('s','sh', name="noah", phone="01048224335")
#joinMember2(id='Hong84', phone='010-1111-2222', job='actor', blood='B')
#example={"name":"Hong", "age":17}
#joinMember2(**example)
#joinMember2(id='Hong84', birth='2024/01/01', blood='A')

'''

#------------------------------------------------------------
# 함수 기능 : 회원 가입 가능
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw, loc, gender
#            선택 => **option => 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일, ......
#            가변 + 데이터 정보 함께
# 반 환 값 : '가입 완료 되었습니다.'str
#------------------------------------------------------------
def joinMember2(id,pw,loc="내국인",gender="남자",**option) :
    # 멤버 저장소에 멤버 추가
    # 키 : id,
    # 값 : pw, loc, gender, **option
    valueDict={}
    valueDict['pw']=pw
    valueDict['loc']=loc
    valueDict['gender']=gender
    valueDict.update(option)
    members[f'{id}']=valueDict
    print(members)

members={}

joinMember2('h','ph') # loc과 gender을 설정하지 않아도 기본값이 있어서 괜찮다
joinMember2('s','sh', name="noah", phone="01048224335")
joinMember2('a','aa', loc="중국", gender="여자", phone='010-1111-2222', job='actor', blood='B')
example={"name":"Hong", "age":17}
#joinMember2(**example)
#joinMember2(id='Hong84', birth='2024/01/01', blood='A')