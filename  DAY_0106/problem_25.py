#25번


def addData(*args) :
    sum,str1=0,''
    if not args :
        print( None)
    elif args[0] in (True, False):
        for data in args:
            sum += int(data)
        print(sum)
    elif str(args[0]).isdecimal() :
        for data in args:
            sum+=data
        print(sum)
    elif str(args[0]).isalnum() :
        for data in args:
            str1+=data
        print(str1)
#2, 9, 3, 5, 8, 7
num_list=list(map(int,input("계산하고 싶은 데이터 입력 :").split(", ")))
addData(*num_list)
addData()
addData(1, 3, 5)
addData(True, True, False, False, True)
addData('A')
addData('A', 'BC', 'Good')