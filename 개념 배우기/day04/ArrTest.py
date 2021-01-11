#ArrTest.py
'''
arData=[[10,11,12,13,14,15,16,17,18,19],
        [20,21,22,23,24,25,26,27,28,29],
        [30,31,32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47,48,49],
        [50,51,52,53,54,55,56,57,58,59]]

#??? 5?? 50??
print(len(arData))     #5
print(len(arData[0]))  #10
print(arData[2][5])

#row : 행
row=2
#col : 열
col=5

arData2=[[0]*col]*row
print(arData2)
'''

'''
arData2=[]
#row : 행
row=2
#col : 열
col=5

for i in range(row):
    arData2.append([])
    for j in range(col):
        arData2[i].append(0)

arData2[0][0]=1
print(arData2)
'''

'''
data1=10
data2=data1
data2+=5

print(data1)
'''

'''
arData1=[10,20,30,40,50]
#arData1의 주소값 = arData2의 주소값
arData2=arData1
aeData2[2]=100

print(arData1[2])
'''

'''
#주소값 말고 값을 복사하는 방법1
arData1=[10,20,30,40,50]
arData2=arData1[:]  #슬라이싱(얕은 복사)
arData2[2]=100
print(arData1[2])

#주소값 말고 값을 복사하는 방법2
import copy
arData1=[10,20,30,40,50]
arData2=copy.copy(arData1) #copy(얕은 복사)
arData2[2]=100
print(arData1[2])
'''

'''
import copy
arData1=[10,[20,30],40]
arData2=copy.copy(arData1)

arData2[0]=100
arData2[2]=400
#[10,[20,30,50],40]
arData2[1].append(50)

print(arData1)
#[10, [20, 30, 50], 40]
print(arData2)
#[100, [20, 30, 50], 400]
'''

'''
#얕은 복사시에는 내부에 존재하는 객체나 리스트 등
#주소값으로 담겨있는 데이터들은 실제 값들까지 복사되지 않고
#주소만 복사되기 때문에 같은 위치를 가르키게 된다.
#따라서 얕은 복사된 객체에서 접근해서 수정을 하게 된다면
#기존데이터에도 수정이 일어나게 된다.

import copy
arData1=[10,[20,30],40]

arData2=copy.deepcopy(arData1)#깊은복사

arData2[0]=100
arData2[2]=400
#[10,[20,30,50],40]
arData2[1].append(50)

print(arData1)
#[10, [20, 30], 40]
print(arData2)
#[100, [20, 30, 50], 400]
'''
