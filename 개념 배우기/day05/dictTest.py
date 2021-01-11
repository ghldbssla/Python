#dictTest.py
'''
arData=[1,2,3,4,5]
for i in range(len(arData)):
    print(arData[i])

for data in arData:
    print(data)
'''
menu={'아메리카노':3500, '카페라떼':4000, '허니브레드':6000}

keys=list(menu.keys())
'''
for i in range(len(keys)):
    print(keys[i],":",menu[keys[i]],"원")

'''
'''
for key in menu.keys():
    print(key,":",menu[key],"원")
'''
#딕셔너리의 경우 빠른 for문으로 안에있는것을 가져오게 되면
#키값을 가져오게 된다.
for key in menu:
    print(key,":",menu[key],"원")


choice= input("주문하실 메뉴")
print(menu[choice],"원 입니다.")
