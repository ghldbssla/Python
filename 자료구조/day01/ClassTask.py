#ClassTask.py
class User:
    userid=''
    userpw=''
    username=''
    usernum=1
    def __init__(self, userid, userpw,username):
        #User.usernum:클래스변수
        self.usernum=User.usernum
        User.usernum+=1
        self.userid=userid
        self.userpw=userpw
        self.username=username

    #return한 문자열이 객체를 출력했을 때 나온다.
    def __repr__(self):
        return str(self.usernum)+"번 회원 : "+self.userid+"("+self.username+")"

user1 = User('apple','1234','김사과')
user2 = User('banana','1234','반하나')
#원래는 주소값으로 만들어져 있는 문자열로 바뀌는 __repr__ 메소드
#재정의를 하면 바꿀수 있다. 오버라이딩!
print(user1)
print(user2)
