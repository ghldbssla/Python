#WhileTest.py
'''
while True:
    print("무한반복")
'''

#while문을 이용해서
#내이름 열번 출력하기
#1.정회윤
#2.정회윤
#...
#10.정회윤

#이름 앞에 붙는 숫자를 나타낼 cnt 변수
cnt=1
#반복 시작
while True:
    print(cnt,". 정회윤",sep="")
    #위에서 출력했을때 10. 정회윤 로 출력했다면 cnt의 값은 10 일것이다.
    #따라서 아래코드에서 cnt가 10이상이라면 더이상 반복하지 않고 탈출하도록
    #만들어준다.
    if(cnt==10):
        break
    #다음 반복때는 cnt 값이 하나 추가된 채 해야하므로
    #반복 마지막에 +1 만큼 증가시켜준다.
    cnt+=1
