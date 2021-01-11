#Bank.py

#class Bank
#변수 : 예금주, 계좌번호, 비밀번호, 잔액
#기능 : 입금, 출금, 잔액조회
import random as r
class Bank:

    def __init__(self,name,account,pw):
        self.name=name
        self.account=account
        self.pw=pw
        self.balance=0
    
    def deposit(self,money):
        self.balance+=money

    def withdraw(self,money):
        if self.balance>=money:
            self.balance-=money
        else:
            print("잔액이 부족합니다.")

    def show(self):
        print(self.name+"님의 계좌번호("+str(self.account)+")")
        print("잔액 :",self.balance)

#국민 : 1000원 넣으면 500원만 입금
class Kookmin(Bank):
    def deposit(self,money):
        self.balance+=(money//2)

#신한 : 500원 출금할 때 1000원 빼기
class Shinhan(Bank):
    def withdraw(self,money):
        money*=2
        Bank.withdraw(self,money)
    
#우리 : 잔액 조회시 잔액 절반으로 줄이기
class Woori(Bank):
    def show(self):
        self.balance//=2
        #self.balance=self.balance//2
        Bank.show(self)

arBank=[[],[],[]]
arCnt = [0,0,0]

def login(account,pw):
    for i in range(len(arBank)):
        for user in arBank[i]:
            if user.account==account:
                if user.pw==pw:
                    #계좌번호와 비밀번호가 일치하는 유저를 찾았다면
                    #그 유저 그대로 리턴
                    return user
    #그 외에는 None 리턴
    return None

def joinView():
    while True:
        print("1. 국민은행\n2. 신한은행\n3. 우리은행\n4. 뒤로가기")
        #선택한 은행을 담을 변수(1:국민은행,2:신한은행,..)
        choice=int(input())
        name = input("이름 : ")
        account = r.randrange(10000,100000)
        pw = input("비밀번호 : ")
        #계좌번호 중복검사를 위한 과정
        while True:
            #True : 중복되지 않음 / False : 중복됨
            check=True
            #모든 유저가 담긴 리스트에서 각 은행별 리스트 하나씩 가져오고
            for i in range(len(arBank)):
                #그 리스트 안에있는 user들을 순회하면서
                for user in arBank[i]:
                    #user의 계좌번호가 랜덤으로 생성된 계좌번호와 같다면(중복된다면)
                    if user.account==account:
                        #계좌 중복되었다는 뜻이므로 계좌번호 새로 생성
                        account=r.randrange(10000,100000)
                        #중복의 의미로 check는 False
                        check=False
                        #이미 중복된것을 알아챘으므로 더이상 반복문을 도는것이 무의미하다
                        #내부 for문 탈출
                        break
                #내부 for문이 끝나고 나왔는데 check가 False라면 중복으로 인한 탈출이다.
                #따라서 이경우에는 i for문을 도는것이 무의미하므로 그것 또한 탈출시켜준다.
                if not check:
                    break
            #i for문이 끝나고 나왔는데 check가 True라는 뜻은, 중복검사를 통과했다는 뜻이므로
            #더이상 위의 과정(중복을 검사하는 과정)을 하지 않도록 무한반복문 탈출
            if check:
                break
        #계좌검사까지 끝났으므로 새로운 user 생성 준비
        newUser=None     
        if choice==1:
            newUser = Kookmin(name,account,pw)
        elif choice==2:
            newUser = Shinhan(name,account,pw)
        elif choice==3:
            newUser = Woori(name,account,pw)
        elif choice==4:
            break
        else:
            print("다시 시도해주세요")
            #잘못 누른경우는 아래 계좌생성을 거치지 않고 다음 반복으로 다시 넘어간다.
            continue
        
        #계좌 생성 시작
        #arBank[choice-1] : 선택한 은행의 유저들이 담기는 리스트
        arBank[choice-1].append(newUser)
        #arCnt[choice-1] : 선택한 은행의 회원 수
        arCnt[choice-1]+=1
        print(newUser.name+"님 계좌 개설 완료!("+str(newUser.account)+")")
        if check:
            break

def loginView():
    account=int(input("계좌번호 : "))
    pw = input("비밀번호 : ")

    #로그인 성공시 : 어떤 user 객체가 담겨왔다
    #실패시 : None값이 담겨있다.
    session=login(account,pw)

    if session is None:
        print("로그인 실패 다시 시도해 주세요")
    else:
        while True:
            #성공시에는 session에 로그인 성공한 유저가 담겨있으므로
            #그대로 session에 . 찍고 사용 가능
            choice = int(input("1. 입금하기\n2. 출금하기\n3. 잔액보기\n4. 로그아웃\n"))
            if choice==1:
                money = int(input("입금하실 금액 : "))
                session.deposit(money)
            elif choice==2:
                money = int(input("출금하실 금액 : "))
                session.withdraw(money)
            elif choice==3:
                session.show()
            elif choice==4:
                print("로그아웃합니다.")
                #session은 로그인 성공한 유저가 담겨있는 곳이므로 로그아웃시에는
                #다시 None으로 바꾸어준다.
                session=None
                break
            
while True:
    print("1. 계좌개설\n2. 로그인\n3. 나가기")
    choice = int(input())
    if choice==1:
        #계좌개설
        joinView()
    elif choice==2:
        #로그인
        loginView()
    elif choice==3:
        print("안녕히가세요")
        break
    else:
        print("다시 시도해주세요")













        
