# sequence type (시퀀스 자료형)
# - str, list, tuple
# - 지정된 값의 순서가 유지
# - 인덱싱과 슬라이싱이 가능
# - 순회(iterable) 가능


# list
# - 여러 값(literal)을 묶어서 관리 (컨테이너 자료형)
# - 특징 : 동적으로 list 크기가 변할 수 있다 (수정 가능)

print("--- list ---")
lst = [1, 2, 3, 4, 5]
print ("list: ", lst)
print ("len(lst): ", len(lst))
print("lst[0]: ", lst[0])
print("lst[1]: ", lst[1])
print("lst[4]: ", lst[4])

# list 저장 요소 추가/수정/삭제
# - list는 동적으로 크기 변경이 가능한 mutable 자료형
# - mutable: list, set, dict
# - immutable: str, int, float, bool, tuple

print("--- list mutable check ---")
print("lst: ", lst)
print("추가 전 id: ", id(lst))

before_id = id(lst)

# list.append(값) : list 끝에 값 추가
lst.append(999)
print("append 후 id: ", lst)
print("append 후 id: ", id(lst))

print('append 전후 같은 list인가? ', before_id == id(lst))

# list.insert(index, 값)
# - index에 값을 삽입하는 메서드
# - 지정된 index 부터 뒤에 있는 모든 list 값의 index가 1씩 밀려난다
print("--- list.insert() ---")
lst.insert(1, 1.5)
lst.insert(0, 0)
print("insert 후: kst", lst)
print("insert 후 lst id: ", id(lst))
print("insert 후 id 비교", before_id == id(lst))

# list update(수정)
# list[인덱스] = 값 (변수에 값 대입해서 변경)
print('--- list update ---')
lst[0] = -10
print("lst: ", lst)

# 특정 인덱스 값 "제거"
# list.pop(index) : 해당 인덱스 값이 제거
# 제거된 index 뒤 요소들을 한 칸씩 당김
print("--- list remove ---")
lst.pop(2)
print("lst: ", lst)
print("id(lst): ", id(lst))

# 2차원 list
# 0차원은 변수 > 1차원 list > 2차원 list > 3차원 list
# 변수는 값을 하나만 저장할 수 있지만
# 1차원 list는 여러 값을 저장할 수 있다
# - 메모리 상에 list는 어떠한 아이디(주소)로 저장됨
# 2차원 list는 7200-7300-7400 이런 식으로 연결되어도
# 아이디(주소)는 각각 아예 다른 번호 저장됨
# lst2[1][3] : 2차원 상의 좌표를 찾음

# 2차원 list
students = [
    ['홍길동', 30],
    ['이순신', 80],
    ['세종대왕', 100]
]
print("students: ", students)
print(students[0][0])
print(students[1][1])
print(students[1])
print(len(students))
print(len(students[2]))

#str.split(구분자)
# -str을 구분자를 기준으로 나눠서 list 형태로 반환
data = "홍길동, 20살, 서울시, 서초구" # csv(Comma Separated Value)
data_ =  data.split(',')
print("data_: ", data_, type(data_))
# list 가 됨

name = data_[0]
age = data_[1]
addr1 = data_[2]
addr2 = data_[3]
print(name, age, addr1, addr2)

# list 슬라이싱 (str 슬라이싱과 방법 동일)
print("--- list slicing ---")
texts = ['lion', 'tiger', 'rabbit', 'horse']

# ['lion', 'tiger]
print(texts [:2])

#['tiger', 'rabbit']
print(texts [1:3])

#['lion', 'rabbit']
print (texts [0:4:2])  # [0::2]

# ['rabbit', 'horse]
print (texts [2:4]) # 끝자리 숫자는 아무거나, [2:]

# slicing 을 이용한 list 값 변경
print (texts)
texts[:2] = ["aaa", "bbb"]
print(texts)
# 0번, 1번 자리를 아예 교체함

# list끼리 더하기(+) 연산
print("--- list 더하기 연산 ---")
a = [10, 20]
b = [30, 40]
a = a+b
print(a) #[10, 20, 30, 40]

b= b + a
print(b) # [30, 40, 10, 20, 30, 40]

# list 순회 (순차 접근, 순차 반복)
# - iterable 특징을 가지는 자료형만 가능
print("--- list 순회 ---")
lst = ['a', 'b', 'c']

# list 요소 순회 : 요소에 하나씩 하나씩 접근한다
for v in lst:
    print(v)
for index, v in enumerate(lst):
    print(f'lst[{index}] : {v}')

# list api

# list.count(값) : list 내에 같은 값이 몇 개 있는가?
print("--- list.count(값) ---")
fruits = ["apple", "banana", "cherry", "apple", "melon"]

print('fruits.count("apple"): ', fruits.count("apple"))
print('fruits.count("kiwi"): ', fruits.count("kiwi"))

# sort : 정렬하다
# list.sort() : 원본 리스트 내에서 정렬(in-place)
# sorted(list) : 정렬된 새 리스트를 반환(not-in-place)
# -> 원본 데이터가 별도로 유지

print("--- list.sort() : 원본 변경 ---")
nums = [100, 30, 50, 20, 70]
print("nums: ", nums)

nums.sort() # 정렬 수행
print("오름차순 정렬된 nums: ", nums)

nums.sort(reverse=True) #정렬 뒤집기 == 내림차순

# key 속성 -> 정렬 기준 함수
print("--- key 속성 -> 정렬 기준 함수 ---")
print("fruits: ", fruits)

# len 함수를 정렬 기준으로 설정
print("--- key 속성-> 정렬 기준 함수 ---")
fruits.append("kiwi")
print("fruits: ", fruits)


# sorted(list) : 원본 유지 정렬

# list unpacking (묶음 풀기)
# - list == 변수의 묶음
numbers = [10, 20, 30]
a, b, c = numbers

# d = 0번 인덱스 요소 (10)
# *e = 나머지 요소 (20, 30) --> [20, 30] 리스트 형태로
d, *e = numbers
print(d,e)

number = [10, 20, 30, 40, 50]
a, *b, c = numbers
# a= 10, b= [20, 30, 40], c= 50