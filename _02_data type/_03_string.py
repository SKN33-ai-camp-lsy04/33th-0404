from jinja2.filters import do_default

my_name = "squirrel"

print ("""
안녕하세요 좋은 하루 보내세요
귀여운 고양이
""")

# 다른 자료형과 연산 불가
# 다른 자료항은 문자형으로 현 변환 이후 연산 가능

# 문자열 반복하기 : *

print ("--- 문자형의 메서드 ---")
# str (문자형, 문자열, String)
# "", '', """, ''' ''' 감싸서 표현

print("=== 작고 아늑한 난쟁이의 집 ====")
s1 = "--- 백설공주가 찾아왔어요 ---"
s2 = "--- 마녀가 독사과를 먹였어요 ---"

print (s1, type(s1))
print (s2, type(s2))

# 삼중 따옴표
print("""
삼중 따옴표는 
입력된 형식 그대로 문자열(str)로 변환
""")
print("""앞/뒤 엔터 없이 작성하려면
따옴표와 문자열을 딱 붙여서 작성""")

# str 연산
# 1. 문자열 + 문자열 = 이어쓰기
print('--- 문자열 더하기 연산 ---')
a = 'apple'
b = 'banana'
print (a + ', ' + b) # apple, banana

# 2. 문자열 * 양의 정수 = 양의 정수 크기 만큼 반복
print ('-' * 10)
# TypeError : unsupported operand types(s) for -: 'str'

# len (객체) : 파이썬 객체 길이 반환
# 파이썬 객체 : str, list, tuple, dict, sset, class 등등
print ('--- len() ---')
text = '귀여운 마카롱'
print (text, len(text))


# --- str 메서드 (str api) ---
# (참고) 함수, 메서드 == 기능 (실행 후 결과 반환)
# api : 문자와 관련된 기능이 제공되어주고 있음

# str.replace (old, new)
# - str 내에서 old에 해당하는 문자를 new로 치환(변경)

# str.strip ([str])
# - 코드 작성법에서 [] 는 생략 가능
# - [str] 생략 시에 공백 제거
print ('---str.strip()---')
some = '            하하하           '
print('[' + some + ']')
print('[' + some.strip() + ']')

origin_str = 'hELLO wORLD!'

print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!


#문자열 포맷팅
x = 10
print("x is %d" %x)    # x is 10

y = "code"
print("y is %s" % y)    # y is code

x, y = 10, "code"

# str. format()
print('--- str.format() ---')
x = 10
y = 1.23
print('{} + {} = {}.format(*args: x, y, x+y')

# f-string (python 3.6~)
print ("---  f-string ---")
print (f"{x} + {y} = {x+y}")

print("x is {0}".format(x))                                        # x is 10
print("x is {0} y is {1}".format(x,y))                             # x is 10 y is code
print("x is {new_x} and y is {new_y}".format(new_x=x, new_y=y))    # x is 10 and y is code