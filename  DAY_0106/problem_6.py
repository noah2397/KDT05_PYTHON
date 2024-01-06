#6번 문제
#datas=['ashed','beach','surf']
#datas=['home','pitch','python']


# datas : ['askde', 'beach', 'surf']  n=2
msg=input()
datas=msg[msg.find('[')+2:msg.find(']')-1].split("', '")
n=int(msg[msg.find('=')+1])

datas.sort(key=lambda x:x[n])
print(datas)