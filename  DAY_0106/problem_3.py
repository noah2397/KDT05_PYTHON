#3번
while True :
    input_case=input()
    if input_case in ['q','Q']:
        break
    elif input_case.isupper() and input_case!='Q':
        print("♠")
    elif input_case.islower() and input_case!='q':
        print("♤")
    elif input_case.isdecimal() :
        print("◎"*int(input_case))