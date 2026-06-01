# list, tuple -> set으로 변경 가능

# 요소 추가 (add)
my_nums = {20,30,40}
my_nums.add(10)
print("my_nums: ", my_nums) # { 10, 20, 30, 40 }

# 요소 제거 (remove)
my_nums.remove(10)

# 전체 제거 (clear)
my_nums.clear()

# set 순회
my num = {30, 50, 70, 90}
#my_nums에서 값을 하나 꺼내서 num 변수에 저장(반복)
for num in my_nums:
    print(num)

# 집합연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합