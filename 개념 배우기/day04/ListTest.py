#ListTest.py

'''
num1=10
num2=20
num3=30
num4=40
num5=50

for i in range(1,6,1):
    print(numi)
'''

'''
arList = [10,20,30,40,50]
print(arList)
for i in range(5):
    print(arList[i])
'''

'''
#비어있는 리스트 만들기
arData1 = []
arData2 = list()

#길이만큼 초기화된 리스트 만들기
arData3=[0]*10
print(arData3)
'''

'''
#list 끝에 값 추가
arData=[]
print(arData)
#맨 뒤에 값을 추가해주는 함수
arData.append(10)
print(arData)
arData.append(20)
arData.append(30)
print(arData)
'''

'''
#list 중간에 값 추가
arData=[]
#(인덱스, 값)으로 삽입함
#해당 인덱스에 있던 값부터 인덱스가 하나씩 밀린다.
arData.insert(0,10)
print(arData)
arData.insert(1,20)
print(arData)
arData.insert(1,30)
print(arData)
'''

'''
#list의 값 수정
arData=[10,20,30,40,50]
arData[2]=100
print(arData)
'''

'''
#list 값 삭제
arData=[10,30,10,20,50]
arData.remove(10)
print(arData)

#list 값 삭제
arData=[10,30,10,20,50]
arData.pop()
print(arData)
'''

'''
#list 값 검색
arData=[10,20,30,40,50]
print(arData.index(30))
#100이 없어서 에러가 남
#print(arData.index(100))
print(100 in arData)
#100이 있는지 true false로 반환
print("a" in "abcd")
#True가 나오므로 문자열도 하나의 문자 list이다!!!!!!!!
'''

'''
#list 값 오름차순 정렬
arData=[1,10,5,7,8,2,4,6,3,9]
arData.sort()
print(arData)
'''

'''
#list 값 내림차순 정렬
arData=[1,10,5,7,8,2,4,6,3,9]
arData.sort()
arData.reverse()
print(arData)
'''

'''
#list의 길이
arData=[10,20,30,40,50]
print(len(arData))
'''

'''
#"문자열".split() 은 통채로가 기준문자열로 나뉜 리스트이다.
dataList="10,20,30,40,50".split(",")
print(dataList[0])
'''

























