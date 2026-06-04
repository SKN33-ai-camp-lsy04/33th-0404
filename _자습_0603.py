print("--- 활력징후를 활용한 list 예제 ---")
vis = ['temperature', 'respiratory rates']
vis.append('pulse')
print(vis)
vis.insert(0, 'mmHg')
print(vis)
vis[1] = 36.5
print(vis)
vis.pop(1)
print(vis)

print("--- 환자&병명을 활용한 2차원 list ---")
ward = [
    ["주은찬", 32],
    ["청가람", 36.5],
    ["현우", 33],
    ["백건", 24]
]
print(ward[1][1])

print("--- 포켓몬을 활용한 2차원 list (2) ---")
pocketmon = [
    ["피카츄", "electronic"],
    ["파이리","fire"],
    ["메타몽", "normal"]
]
print(pocketmon[0][0], " is cute")
print("Why ", pocketmon[2][0], "is ", pocketmon[2][1], "type? It doesn't look like.")

print("--- 사신 후계자를 이용한 2차원 list (3) ---")
four = [
    ["주은찬", "fire", "phynix", "kind"],
    ["청가람", "electronic", "dragon", "cooking"],
    ["현우", "death", "turtle", "memorizing"],
    ["백건", "strong", "tiger", "punch"]
]

print(four[0][0]," can use the ", four[0][1])
print("One is", four[0][3], " and One is ", four[3][3])
print(""" """)
print( four[1][0], "is good at ", four[1][3])

print("--- 알파벳을 이용한 구분자 연습 ---")
alpha = ['a', 'b', 'c', 'd', 'e']
alpha2 = ['f', 'g', 'h', 'i', 'j']
alpha3 = ['k', 'l', 'm', 'n', 'o']
alpha4 = ['p', 'q', 'r', 's', 't']
alpha5 = ['u', 'v','w', 'x', 'y', 'z' ]
print(alpha2[3], " ", alpha3[1], alpha3[4], alpha5[1], alpha[4], " ",
      alpha5[4], alpha3[4], alpha5[0])
print(alpha3[2], alpha[0], alpha4[3], alpha4[4], alpha[4], alpha4[2])
print(alpha3[3:5])
print(alpha5[1:6:2])
print(alpha4[0:3:2], alpha2[3], alpha3[3], alpha[2:5:2], alpha4[3]*2)
print(alpha5[3::])

print("--- 우유를 활용한 리스트 더하기 ---")
milk = ['basic', 'strawberry', 'choco']
tea = ['milktea']
milk = milk + tea
print(milk)

print("--- 꽃을 이용한 list 요소 순회 ---")
flower = ['개나리', '진달래', '해바라기', '민들레']
for v in flower:
    print('개나리')

print("--- 시를 활용한 count ---")
poem = ("꽃", "은", "예", "뻐", "도", "행복하지", "않다",
        "별", "은", "높", "아", "도", "행복하지", "않다")
print(poem.count("은"))
print(poem.count("도"))
print(poem.count("행복하지"))
print(poem.count("않다"))

print("--- 물가를 활용한 sort & unpacking ---")
price = [
    ['삼각김밥', 1200],
    ['푸딩', 3500],
    ['라면', 1800],
    ['콜라 1.5리터', 3000],
    ['생리대 중형', 9900]
]
price2 = [price[0][1], price[1][1], price[2][1], price[3][1], price[4][1]]
price2.sort()
print(price2)
price2.sort(reverse=True)
print(price2)

product = [price[0][0], price[1][0], price[2][0], price[3][0], price[4][0]]
product.sort(key=len)
print(product)

a, b, c, d, e = product
print(a, c)


print("--- list 복습을 완료했습니다. 축하합니다! ---")