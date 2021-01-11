#setTest.py

arSet={1, 2, 3, 4, 5}

#셋에 값 추가하기
arSet.add(6)
arSet.add(1)
arSet.add(1)
arSet.add(1)
arSet.add(1)
arSet.update([1,3,5,7,9,10])
print(arSet)

#셋 값 수정하기
#인덱싱이 불가능하기 때문에 list로 형변환 한 후
arSet=list(arSet)
#값을 수정하고
arSet[1]=100
#다시 Set으로 형태를 변환해 준다.
arSet=set(arSet)
print(arSet)

#셋 값 삭제하기
arSet.remove(100)
print(arSet)

#셋을 이용한 필터링
print(list(set([1,1,1,1,1,1,1,1])))
#============================
s1={1,2,4,10,7,100}
s2={2,10,100,6,1000}

#교집합
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2))

#차집합
print(s1-s2)
print(s1.difference(s2))

















