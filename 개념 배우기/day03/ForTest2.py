#ForTest2.py

'''
for i in range(10):
    if(i==3):
        continue
    print(i+1)
'''
##range(횟수)만 이용해서 만들어보기!

# 0~10 출력하기
'''
for i in range(11):
    print(i)
'''

#10~0 출력하기
'''
for i in range(11):
    print(10-i)
'''

#n 입력받아서 1~n 출력하기
'''
n=int(input("n = "))
for i in range(n):
    print(i+1)
'''
#---------------------------1--------------------------
#1~10 까지의 합 출력하기
'''
n=0
for i in range(11):
    n+=i
print(n)
'''

#n과 m 입력받아서 n~m 합 출력하기
'''
n=int(input("n = "))
m=int(input("m = "))
sum=0
for i in range(m+1):
    if(i<n):
        continue
    sum+=i
print(sum)
'''

#1~100사이의 짝수만 출력하기
'''
for i in range(50):
    print((i+1)*2)
'''

#1~100사이에서 6과 9의 공배수 출력하기
'''
for i in range(100):
    if(i%6==0 and i%9==0 and i>0):
        print(i)
'''
#---------------------------2--------------------------
#A~F 출력하기
'''
for i in range(71):
    if(i<65):
        continue
    print(chr(i))
'''

#A~F 중 D 건너뛰고 출력하기
'''
for i in range(71):
    if(i==68 or i<65):
        continue
    print(chr(i))
'''

#AbCdEfGh...z 출력하기
'''
for i in range(26):
    if(i%2==0):
        print(chr(65+i))
    else:
        print(chr(97+i))
'''
#---------------------------3--------------------------













