#ForTest.py

'''
#1부터11 전까지 : 10번 반복
#내부에서 i 가 1~10까지 1씩 증가한다.
for i in range(1,11,1):
    print(i,".정회윤",sep='')

#1부터11 전까지 : 10번 반복(증가량이 1로 고정)
for i in range(1,11):
    print(i,".정회윤",sep='')


#range(0,10,1)와 동일
for i in range(10):
    print(i+1,".정회윤",sep='')
    
'''

for i in range(10,0,-1):
    print(i)

for i in range(0,101,2):
    print(i)
