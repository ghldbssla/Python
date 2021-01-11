#dictionarytest.py

arDict={'walk':'걷다', 'fly':'날다', 'run':'달리다'}

#딕셔너리 사용
print(arDict['walk'])

#딕셔너리에 값 추가
arDict['play'] = '놀다'
print(arDict)

#딕셔너리 값 수정
arDict['run'] = '뛰다'
print(arDict)

#dict.keys()
keys=list(arDict.keys())
print(keys[1])

#dict.values()
values=list(arDict.values())
print(values[1])

#dict.items()
items = list(arDict.items())
for i in range(len(items)):
    print("keys : ",items[i][0])
    print("values : ",items[i][1])
    
