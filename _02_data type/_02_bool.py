# A == B : A, B가 같으면 True, 아니면 False

print("1>0.5", 1<0.5) # True

# 논리 부정 연산 (not)
print(True)
print(not True)
print(not not True)

# and 연산
# - A가 참이고 B도 참인 경우에 참
# T and T == T
# T and F == F
# F and T == F
# F and F == F

print('--- and ---')
print(100 > 0 and 1 == 1) # True
print(30 > 20 and 123 != 123) # False
print(3 <= -3 and 12 > 12) # False
print(9 >= 9 / 9*9 and 12 != 12+1)

# or 연산
# A 또는 B가 True이면 결과도 True
# <-> A와 B가 모두 False이면 False
# T or T == T
# T or F == T
# F or T == T
# F or F == F

print('--- or ----')
print(100 > 0 or 1 == 1)
print(10*10 == 100 or 1 != 1)
print(100 == 0 or 10 == 10)
print(10 + 20  * 5 == 100 or 30 / 10 + 5 == 2) # False


# 60점 이상 입력 시 합격(True) 아니면 불합격(False)
print ("--- 합격/불합격 ---")
score = int(input('점수를 입력하세요: '))
print (score, type(score))
# input() 함수 : 키보드 입력을 받는 함수 (str로 저장)
# int() 함수 : str->int로 변환

result = score >= 60
# print( "합격 여부 : ", result)

print ("합격 여부 : ", '합격' if result == True else '불합격')
