#MyExcTask.py

#내 예외클래스 만들어서
#채팅 치다가 "바보", "멍청이" 라는 말을 하면
#필터링 시키고 예외 발생 시키기
class MyException(Exception):
    #객체 출력시 나올 문자열을 정의해 줄 수 있는 메소드
    def __str__(self):
        return "비속어 금지"
    #__repr__

def filtering(msg):
    badwords=["바보","멍청이"]
    for word in badwords:
        if (word in msg):
            #예외 발생
            raise MyException
cnt=0
while True:
    try:
        chat=input("채팅 : ")
        filtering(chat)
        print(chat)
    except MyException as me:
        cnt+=1
        print(me)
        print("경고 X",cnt,sep="")
        if(cnt==3):
            print("강퇴합니다.")
            break
    except KeyboardInterrupt:
        print("프로그램을 종료합니다.")
        break
    except Exception as e:
        print(e)






