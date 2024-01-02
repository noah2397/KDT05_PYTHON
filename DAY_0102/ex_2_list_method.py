#-----------------------------------------------------
# 메서드 => 특정 데이터 타입의 전용 함수를 메서드(Method)라고 부름
# - 범용의 함수와 식별하기 위해서 지정한 호칭이다
# - 사용법 : 데이터.메서드명 or 변수명.메서드명
#------------------------------------------------------
# List 전용 메서드 살펴보기 ===========================
# [1] 리스트에 데이터 추가해주는 메서드 => append() 맨끝에 원소로 추가
nums=[0]
'''
print(f'nums : {len(nums)}개, {nums}')  # 범용이라 문법이 특정 데이터타입의 메서드와 다르다
print(f"nums.index(60) : {nums.index(60)}번째에 60 요소가 존재함")
nums.append("99")
print(f'nums : {len(nums)}개, {nums}')

# [2] 리스트에 데이터 추가해주는 메서드 => insert(위치인덱스, 데이터) 지정 위치에 추가
nums.insert(3, 1024)
print(f'nums : {len(nums)}개, {nums}') # 3번 인덱스 자리에 1024가 들어가있음을 확인할 수 있다

nums.insert(-1, ['ABC','DEF'])
print(f'nums : {len(nums)}개, {nums}') # 리스트 형태가 하나의 요소로 들어감을 확인할 수 있다





# "DEF"
del nums[-2][-1]
print(f'nums : {len(nums)}개, {nums}') # 지워도 원소 개수가 줄어들진 않는다

# 리스트 안에 모든 원소 삭헤쟇서ㅓ 빈 리스트 만들어주세요
del nums[:]
print(f'nums : {len(nums)}개, {nums}')

#리스트 안에 원소/요소 정렬해주는 메서드 => sort() 오름차순 정렬
# - 오름차순 : 작은 데이터 >>> 큰 데이터
nums.append(98)
nums.append(-2)
nums.append(4)
nums.append(0)
nums.append(0.1)
print(nums)
nums.sort()
print(nums)

# 내림차순 : 큰 데이터 >> 작은 데이터 순서로
nums.sort(reverse=True) #역순으로 정렬
print(nums)
'''
# nums=[0,1,2,3,4,5,60,7,8]
# # [4] 리스트 안에 원소/요소의 현재 위치를 반대로 뒤집어주는 메서드 => reverse()
# # 원소/요소 데이터 값 비교 안함!! 순서만 변경함!!
# nums.reverse()
# print(f'nums : {len(nums)}개, {nums}')
#
# # [5] 리스트 안에 원소/요소를 삭제해주는 메서드 => remove(데이터)
# # - 리스트에서 지정된 값의 원소 삭제
# # - 없는 값을 지우려고 하면 에러 발생
# nums.remove(0) # 값을 가지고 삭제한다
# print(f'nums : {len(nums)}개, {nums}')  # 0이라는 값을 지움
# nums.remove(0) # 또 지우려는데 0인 값이 없어서 에러 반환

# nums.clear()
# print(nums)
#
#
# # [6] 리스트에 원소/요소를 꺼내는 메서드 => pop(인덱스)
# nums=[10,-3,7]
# pop_item = nums.pop()
# print(f'popitem : {pop_item}, nums : {len(nums)}개, {nums}')
#
# # [7] 리스트에서 특정 원소/요소 데이터가 몇 개 존재하는지  세주는 메서드 => count(데이터)
# print(nums.count('A'))
# print(nums.count(10))
#
# # [8] 리스트를 확장시키는 메서드 => extend(여러개 데이터 저장한 데이터 타입)
# nums.extend([])
# print(f'nums : {len(nums)}개, {nums}')
#
# nums.extend("새해 복 많이 받으세요.")
# print(f'nums : {len(nums)}개, {nums}')
#
# nums.extend(["새해 복 많이 받으세요."])
# print(f'nums : {len(nums)}개, {nums}')
#
# #nums.extend(2024) # 에러가 뜬다 => 리스트가 아니기 때문
# print(f'nums : {len(nums)}개, {nums}')

# [9] 리스트를 복사해주는 메서드 => 얕은 복사 copy()
nums=[0]
nums2=nums
nums[-1]=3049 # 똑같은 주소를 할당해서 값을 바꾸면 다른 리스트도 동시에 업데이트
print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')


# nums의 -1번 요소의 데이터를 2024로 변경
nums2=nums.copy() # 다른 주소를 할당해서 값을 복사하므로 다른 리스트에 영향을 주지 않음
nums[-1]=2024
print(f'nums : {len(nums)}개, {nums}')
print(f'nums2 : {len(nums2)}개, {nums2}')