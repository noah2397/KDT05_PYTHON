# 코딩도장 p.150 심사문제

#1번째 방법
# 입력 : health health_regen mana mana_regen
#       575.6 1.7 338.8 1.63
#key_list=['health','health_regen','mana','mana_regen']
#value_list=[575.6, 1.7, 338.8, 1.63]
'''
key_list=input().split()
value_list=input().split()
dict_sum=dict(zip(key_list, value_list))
print(dict_sum)
'''

#2번째 방법
'''
key_list=input().split()
value_list=input().split()
dict_sum=dict()
for i in range(len(key_list)):
    dict_sum[key_list[i]]=value_list[i]
print(dict_sum)
'''

#3번째 방법
'''
key_list=input().split()
value_list=input().split()
dict_sum=dict()
dict_sum[key_list[0]]=value_list[0]
dict_sum[key_list[1]]=value_list[1]
dict_sum[key_list[2]]=value_list[2]
dict_sum[key_list[3]]=value_list[3]
print(dict_sum)
'''
