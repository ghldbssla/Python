n=input()
num=0

for i in range(len(n)):
     if("U" in n[i] and num==0):
          num=1
     if("C" in n[i] and num==1):
          num=2
     if("P" in n[i] and num==2):
          num=3
     if("C" in n[i] and num==3):
          num=4

if(num==4):
     print("I love UCPC")
else:
     print("I hate UCPC")
