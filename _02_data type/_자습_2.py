from mimetypes import init

from six import PY34

Hr = [100, 140, 160, 60, 80, 200, 110]
Tp = [31, 32, 33, 34, 35, 36, 37]
Pu = [10, 12, 14, 16, 18, 20, 22]

Hr.sort()
print("심박수: ", Hr)












H = init(input("심박수를 입력하세요: "))
T = init(input("체온을 입력하세요: "))
P = init(input("맥박을 입력하세요: "))
R = init(input("호흡수를 입력하세요: "))

temperature = b
pulse = c
respiratory_rates = d

lst = [
    [ a , 90, 140],
    [ b , 35, 37.5],
    [ c , 60, 100],
    [ d , 12, 20]
]

P1 = a < 90 or a >140
P2 = b < 35 or b > 37.5
P3 = c < 60 or c > 100
P4 = d < 12 or d > 20

result = x
Problem = P1 or P2 or P3 or P4
print("활력징후 결과 : 이상있음" if result == Problem else "활력징후 결과 : 정상")

