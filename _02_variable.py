# 변수 (variable)
# 값(literal)을 저장하는 메모리 상의 공간
# 각 변수마다 이름이 지정되어 있음 (이름을 불러서 사용)


# 변수 선언 방법
# 변수명 = 값
a = 10  # a라는 메모리 상의 공간에 10(literal)을 대입해라
b = '홍길동'

print("a =", a)
print("b =", b)


# 대입 연산지(=)
# 우항의 값을 좌항의 변수에 대입 (무조건 오른쪽 -> 왼쪽)
num = 100
print("num =", num)

# 변수는 저장된 값이 계속 변할 수 있다
num = 1201
print("num = ", num)

num = "love u"
print("num =", num)


## 변수 명명 규칙
#1. 의미 있는 이름 사용
#2. 변수명은 snake case를 사용 (소문자와 _)
# 단, 대문자도 사용은 가능하고 소문자와 구분된다

team_name = "오지라퍼스"
print(team_name)    # 오지라퍼스

Team_name = "Ohgiraffers"
print(team_name)    # 오지라퍼스
print(Team_name)    # Ohgiraffers

# 한글 변수명은 인코딩 등의 문제를 야기할 수 있으므로 사용을 지양한다

Fri = "alone"
Sat = "together"
print ("Fri =", Fri)
print ("Sat =", Sat)
print ("행복해")

# 변수명은 숫자로 시작해서는 안 된다 (문법 오류 == 빨간줄)
# 1_name = "팥쥐" # 문법 에러

# 특수 문자는 언더스코어(_)를 제외하고 사용 불가

# 예약어는 변수명으로 사용 불가능

if
for
elif
while
else

