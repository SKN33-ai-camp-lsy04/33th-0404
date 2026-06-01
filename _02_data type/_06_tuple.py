# tuple
# - 변경불가 (immutable)한 list
# - sequence type (indexing, slicing, iterable)
# - 주로 함수 반환 값, 안전한 데이터 집합을 만들 때 사용

print ("--- tuple ---")
t1 = () # 비어있는 tuple
t2 = (10) #  == (int) 10과 같음
t3 = (10,) # (tuple)(10) 과 같음
t4 = (10, 20)
t5 = 10, 20 # ()를 생략 -> 자동 packing

print(t1, type(t1))
print(t2, type(t2))
print(t3, type(t3))
